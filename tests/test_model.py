"""Tests de non-régression du modèle et des générateurs (unittest, sans dépendance)."""
from __future__ import annotations

import copy
import pathlib
import sys
import tempfile
import unittest
import xml.dom.minidom

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "tools"))

import generate_polarion  # noqa: E402
from almmodel import NATIVE_FIELDS, load_model, validate  # noqa: E402


class ModelValidationTest(unittest.TestCase):
    def setUp(self):
        self.model = load_model()

    def test_model_is_consistent(self):
        m = validate(load_model())
        self.assertEqual(m.errors, [], "\n".join(m.errors))

    def test_every_type_has_core_fields(self):
        for t in self.model.types:
            if t["family"] == "library":
                continue
            ids = self.model.field_ids_of(t["id"])
            for f in ("discipline", "informationClassification", "exportControl"):
                self.assertIn(f, ids, f"{t['id']} sans {f}")

    def test_safety_flags_default_to_tbd(self):
        opts = self.model.enumerations["yesNoTbd"]["options"]
        default = [o["id"] for o in opts if o.get("default")]
        self.assertEqual(default, ["tbd"], "Principe P4 : aucune valeur de sûreté affirmative par défaut")

    def test_non_negotiable_core_in_every_class(self):
        for cid, prof in self.model.tailoring["classProfiles"].items():
            wits = prof["workItemTypes"]
            if wits == "all":
                continue
            for core in ("nonConformance", "verificationCase", "deliverable"):
                self.assertIn(core, wits, f"{cid} : {core} manquant")

    def test_approval_transitions_enforce_independence(self):
        """Socle NN-02 : toute transition signée 'verified' ou 'approved' exige l'indépendance."""
        exempt = {("wfDeliverable", "submit"), ("wfAnalysis", "submit"),
                  ("wfDocumentFull", "submitVerification"), ("wfDocumentLight", "submit"),
                  ("wfDocumentLibrary", "submit"), ("wfChangeRequest", "approve"),
                  ("wfChangeRequest", "reject"), ("wfReview", "close"),
                  ("wfWaiver", "approveExternal"), ("wfCommitment", "cancel"),
                  ("wfLibraryItem", "publish"), ("wfInterface", "agree"),
                  ("wfAnomaly", "close"), ("wfNonConformance", "close"),
                  ("wfNonConformance", "cancel")}
        for wid, wf in self.model.all_workflows().items():
            for tr in wf["transitions"]:
                sig = tr.get("signature") or {}
                if not sig.get("required") or sig.get("meaning") not in ("verified", "approved", "safety"):
                    continue
                if (wid, tr["id"]) in exempt:
                    continue
                keys = {k for c in tr.get("conditions", []) or [] for k in c}
                self.assertIn("approverNotAuthor", keys, f"{wid}.{tr['id']} sans contrôle d'indépendance")

    def test_validator_detects_unknown_enum(self):
        m = load_model()
        m.types = copy.deepcopy(m.types)
        m.types[0]["fields"].append({"id": "bogus", "type": "enum:doesNotExist", "fr": "x", "en": "x"})
        validate(m)
        self.assertTrue(any("énumération inconnue" in e for e in m.errors))

    def test_validator_detects_native_field_redefinition(self):
        m = load_model()
        m.types = copy.deepcopy(m.types)
        m.types[0]["fields"].append({"id": "status", "type": "string", "fr": "x", "en": "x"})
        validate(m)
        self.assertTrue(any("champ natif" in e for e in m.errors))

    def test_validator_detects_unreachable_state(self):
        m = load_model()
        m.workflows = copy.deepcopy(m.workflows)
        m.workflows["wfAction"]["states"].append({"id": "orphan", "fr": "x", "en": "x", "category": "done"})
        validate(m)
        self.assertTrue(any("inatteignable" in e for e in m.errors))


class GenerationTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.tmp = tempfile.TemporaryDirectory()
        cls.out = pathlib.Path(cls.tmp.name)
        for lang in ("fr", "en"):
            rc = generate_polarion.main(["--lang", lang, "--out", str(cls.out / lang)])
            assert rc == 0
        cls.model = load_model()

    @classmethod
    def tearDownClass(cls):
        cls.tmp.cleanup()

    def test_all_xml_well_formed(self):
        files = list(self.out.rglob("*.xml"))
        self.assertGreater(len(files), 200)
        for f in files:
            xml.dom.minidom.parse(str(f))

    def test_expected_files_exist(self):
        base = self.out / "fr" / ".polarion"
        self.assertTrue((base / "tracker/fields/workitem-type-enum.xml").exists())
        self.assertTrue((base / "tracker/fields/workitem-link-role-enum.xml").exists())
        self.assertTrue((base / "documents/fields/document-type-enum.xml").exists())
        self.assertTrue((base / "testing/configuration/testrun-status-enum.xml").exists())
        for t in self.model.types:
            for p in (f"tracker/fields/{t['id']}-custom-fields.xml",
                      f"tracker/fields/{t['id']}-status-enum.xml",
                      f"tracker/workflow/{t['id']}-workflow.xml"):
                self.assertTrue((base / p).exists(), p)

    def test_workflow_required_fields_exist_on_type(self):
        base = self.out / "fr" / ".polarion" / "tracker"
        for t in self.model.types:
            doc = xml.dom.minidom.parse(str(base / "workflow" / f"{t['id']}-workflow.xml"))
            custom = self.model.field_ids_of(t["id"])
            for f in doc.getElementsByTagName("field"):
                name = f.getAttribute("name")
                self.assertTrue(name in custom or name in NATIVE_FIELDS, f"{t['id']}: {name}")

    def test_document_workflow_required_fields_exist(self):
        doc_fields = {f["id"] for f in self.model.document_types["documentCustomFields"]}
        base = self.out / "fr" / ".polarion" / "documents" / "workflow"
        for f in base.glob("*-workflow.xml"):
            doc = xml.dom.minidom.parse(str(f))
            for fld in doc.getElementsByTagName("field"):
                name = fld.getAttribute("name")
                self.assertTrue(name in doc_fields or name in {"title", "status"}, f"{f.name}: {name}")

    def test_no_purely_negative_queries(self):
        for f in (self.out / "fr" / ".polarion").rglob("*-workflow.xml"):
            doc = xml.dom.minidom.parse(str(f))
            for p in doc.getElementsByTagName("param"):
                if p.getAttribute("name") == "query":
                    self.assertFalse(p.getAttribute("value").strip().startswith("NOT "), f.name)

    def test_cross_project_roles_allow_other(self):
        doc = xml.dom.minidom.parse(str(self.out / "fr/.polarion/tracker/fields/workitem-link-role-enum.xml"))
        for opt in doc.getElementsByTagName("option"):
            if opt.getAttribute("id") == "verifies":
                targets = " ".join(r.getAttribute("to") for r in opt.getElementsByTagName("rule"))
                self.assertIn("__other", targets)
                return
        self.fail("rôle verifies absent")

    def test_labels_follow_language(self):
        fr = (self.out / "fr/.polarion/tracker/fields/workitem-type-enum.xml").read_text(encoding="utf-8")
        en = (self.out / "en/.polarion/tracker/fields/workitem-type-enum.xml").read_text(encoding="utf-8")
        self.assertIn("Exigence système", fr)
        self.assertIn("System requirement", en)


if __name__ == "__main__":
    unittest.main()
