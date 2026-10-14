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

    def test_technical_check_transitions_enforce_independence(self):
        """Socle NN-02 : toute transition de contrôle technique exige l'indépendance auteur ≠ vérificateur."""
        flagged = 0
        for wid, wf in self.model.all_workflows().items():
            for tr in wf["transitions"]:
                if tr.get("technicalCheck"):
                    flagged += 1
                    keys = {k for c in tr.get("conditions", []) or [] for k in c}
                    self.assertIn("approverNotAuthor", keys, f"{wid}.{tr['id']}")
        self.assertGreaterEqual(flagged, 20)

    def test_state_ids_have_single_meaning(self):
        cats = {}
        for wf in self.model.all_workflows().values():
            for st in wf["states"]:
                cats.setdefault(st["id"], set()).add(st["category"])
        self.assertEqual({k: v for k, v in cats.items() if len(v) > 1}, {})

    def test_every_project_type_fully_covered(self):
        m = validate(load_model())
        cov_errors = [e for e in m.errors if e.startswith("couverture")]
        self.assertEqual(cov_errors, [])
        project_types = {o["id"] for o in self.model.enumerations["projectType"]["options"]}
        self.assertEqual(project_types, set(self.model.coverage["scenarios"]))

    def test_coverage_detects_tailoring_regression(self):
        """Retirer le composant physique du profil express doit casser le scénario fortuit."""
        m = load_model()
        m.tailoring = copy.deepcopy(m.tailoring)
        m.tailoring["classProfiles"]["classD"]["workItemTypes"].remove("physicalComponent")
        validate(m)
        self.assertTrue(any(e.startswith("couverture fortuit") for e in m.errors))

    def test_required_fields_do_not_block_imports(self):
        m = load_model()
        m.field_sets = copy.deepcopy(m.field_sets)
        for f in m.field_sets["common"]["fields"]:
            if f["id"] == "discipline":
                f["required"] = True
        validate(m)
        self.assertTrue(any("obligatoire à la création sans défaut" in e for e in m.errors))

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

    # ------------------------------------------------------------ ajouts v0.3
    def test_yaml_yes_no_stay_strings(self):
        """YAML 1.1 lit yes / no comme booléens : les identifiants d'énumération doivent rester textuels."""
        ids = [o["id"] for o in self.model.enumerations["yesNoTbd"]["options"]]
        self.assertEqual(ids, ["tbd", "yes", "no"])
        for eid, e in self.model.enumerations.items():
            for o in e["options"]:
                self.assertIsInstance(o["id"], str, f"{eid}: {o['id']!r}")

    def test_templates_inherit_from_master(self):
        m = self.model
        for t in m.topology["projectTemplates"]:
            chain = m.template_chain(t["id"])
            self.assertEqual(m.template_level(chain[-1]), "master", chain)
        for pt, d in m.tailoring["projectTypeDefaults"].items():
            self.assertIsNotNone(m.archetype_of(d["template"]), f"{pt} sans archétype")

    def test_every_regulatory_framework_has_pack(self):
        frameworks = {o["id"] for o in self.model.enumerations["regulatoryFramework"]["options"]}
        self.assertEqual(frameworks, set(self.model.regulatory_packs["packs"]))

    def test_pack_hidden_field_cannot_be_required(self):
        """Un champ propre à un pays ne doit pas bloquer les projets des autres juridictions."""
        m = load_model()
        m.workflows = copy.deepcopy(m.workflows)
        tr = next(t for t in m.workflows["wfChangeRequest"]["transitions"] if t["id"] == "toCcb")
        tr["requiredFields"].append("regulatoryModificationClass")
        validate(m)
        self.assertTrue(any("champ masqué" in e for e in m.errors))

    def test_cross_project_trace_needs_cross_project_role(self):
        m = load_model()
        m.link_roles = copy.deepcopy(m.link_roles)
        next(r for r in m.link_roles if r["id"] == "supersedes").pop("crossProject")
        validate(m)
        self.assertTrue(any("non déclaré crossProject" in e for e in m.errors))

    def test_import_profiles_reference_model_fields(self):
        m = load_model()
        m.import_export = copy.deepcopy(m.import_export)
        m.import_export["reqif"]["profiles"][0]["mapping"].append({"reqif": "X", "field": "doesNotExist"})
        validate(m)
        self.assertTrue(any(e.startswith("ReqIF RIF-CUSTOMER-IN") for e in m.errors))

    def test_work_package_matrix_traces(self):
        m = self.model
        self.assertTrue(m.link_allowed("deliverable", "inWorkPackage", "workPackage"))
        self.assertTrue(m.link_allowed("analysis", "inWorkPackage", "workPackage", cross_project=True))
        self.assertIn("workPackage", m.effective_profile("componentManufacturing")[0])


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
