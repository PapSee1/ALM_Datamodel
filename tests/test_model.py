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

    # ------------------------------------------------------------ ajouts v0.4
    def test_nuward_pilot_derivation(self):
        m = validate(load_model())
        pilot = next(p for p in m.pilots if p["id"] == "P-NUWARD-L1")
        d = pilot["derived"]
        self.assertEqual((d["projectClass"], d["instance"], d["archetype"]), ("classA", "STD", "TPL-01-PRODUCT"))
        self.assertEqual(d["extProject"], "TPL-EXT")
        self.assertIn("workPackage", d["enableTypes"])
        self.assertIn("cfr5059Screening", d["hiddenFields"])

    def test_pilot_must_keep_non_negotiable_core(self):
        m = load_model()
        m.pilots = copy.deepcopy(m.pilots)
        m.pilots[0]["pilotScope"]["activeTypes"].remove("nonConformance")
        validate(m)
        self.assertTrue(any("socle non négociable non activé" in e for e in m.errors))

    def test_pilot_detects_workflow_dependency_on_inactive_type(self):
        m = load_model()
        m.pilots = copy.deepcopy(m.pilots)
        m.pilots[0]["pilotScope"]["activeTypes"].remove("action")
        validate(m)
        self.assertTrue(any("dépend du type non activé action" in e for e in m.errors))

    def test_every_type_has_deployment_increment(self):
        m = load_model()
        m.extension_policy = copy.deepcopy(m.extension_policy)
        m.extension_policy["deploymentIncrements"][-1]["types"] = []
        validate(m)
        self.assertTrue(any("sans incrément de déploiement" in e for e in m.errors))

    def test_local_prefix_never_used_by_core(self):
        prefix = self.model.extension_policy["localFieldPrefix"]
        for t in self.model.types:
            for f in self.model.field_ids_of(t["id"]):
                self.assertFalse(f.startswith(prefix), f)

    # ---- v0.5 : état de soumission, champs requis, cascade, pseudo-rôles, seuils ----

    def test_every_workitem_workflow_declares_submit_state(self):
        """Principe P7 : chaque workflow de Work Item a un état de soumission atteint par une transition."""
        for wid, wf in self.model.workflows.items():
            sub = wf.get("submitState")
            self.assertTrue(sub, f"{wid} sans submitState")
            self.assertIn(sub, {st["id"] for st in wf["states"]}, f"{wid}: submitState inconnu")
            self.assertTrue(any(tr["to"] == sub for tr in wf["transitions"]), f"{wid}: aucune transition vers {sub}")

    def test_validator_detects_unknown_required_at(self):
        m = load_model()
        t = m.type_by_id("function")
        for f in t["fields"]:
            if f["id"] == "functionLevel":
                f["requiredAt"] = "etatInexistant"
        m = validate(m)
        self.assertTrue(any("requiredAt" in e for e in m.errors), "\n".join(m.errors))

    def test_deferred_state_is_open_and_anomaly_uses_waived(self):
        cr = {st["id"]: st for st in self.model.workflows["wfChangeRequest"]["states"]}
        self.assertEqual(cr["deferred"]["category"], "open")
        an = {st["id"] for st in self.model.workflows["wfAnomaly"]["states"]}
        self.assertIn("waived", an)
        self.assertNotIn("deferred", an)

    def test_document_cascade_declarations_are_consistent(self):
        for d in self.model.document_types["documentTypes"]:
            cascade = d.get("cascadeTypes") or []
            self.assertIn(d["primaryType"], self.model.type_ids, d["id"])
            self.assertIn(d["primaryType"], d.get("allowedTypes") or [d["primaryType"]], d["id"])
            for t in cascade:
                self.assertIn(t, self.model.type_ids, f"{d['id']}: {t}")
            for t, statuses in (d.get("approvalGate") or {}).items():
                self.assertIn(t, self.model.type_ids, f"{d['id']}: approvalGate {t}")
                wf = self.model.all_workflows()[self.model.type_by_id(t)["workflow"]]
                for st in statuses:
                    self.assertIn(st, {x["id"] for x in wf["states"]}, f"{d['id']}: approvalGate {t} statut {st}")

    def test_pseudo_roles_are_the_expected_ones(self):
        pseudo = {r["id"] for r in self.model.roles["projectRoles"] if r.get("pseudo")}
        self.assertEqual(pseudo, {"anyProjectMember", "documentOwner", "workitem.assignee", "workitem.author"})
        self.assertFalse(any(r.get("pseudo") for r in self.model.roles["globalRoles"]))

    def test_derive_project_reads_thresholds_from_yaml(self):
        import model_checks
        m = validate(load_model())
        answers = copy.deepcopy(m.pilots[0]["answers"])
        self.assertEqual(model_checks.derive_project(m, answers)["projectClass"], "classA")
        m.tailoring["scoringGrid"]["thresholds"]["classA"]["min"] = 100
        self.assertEqual(model_checks.derive_project(m, answers)["projectClass"], "classB")


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

    def test_project_kit_is_a_subset_of_core(self):
        import generate_project
        m = validate(load_model())
        pilot = m.pilots[0]
        base = self.out / "project" / ".polarion"
        files = generate_project.project_files(m, pilot, "fr", base)
        allowed = ("tracker/fields/workitem-type-enum.xml", "documents/fields/document-type-enum.xml")
        for f in files:
            xml.dom.minidom.parse(str(base / f))
            self.assertTrue(f in allowed or f.endswith("-enum.xml") or f.endswith("-custom-fields.xml"), f)
        dom = xml.dom.minidom.parse(str(base / "tracker/fields/workitem-type-enum.xml"))
        ids = {o.getAttribute("id") for o in dom.getElementsByTagName("option")}
        self.assertEqual(ids - {"heading"}, set(pilot["pilotScope"]["activeTypes"]))

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

    # ---- v0.5 : scripts dérivés, cascade, signatures, langue, manifeste ----

    def _wf(self, lang: str, name: str) -> str:
        return (self.out / lang / ".polarion" / "tracker" / "workflow" / f"{name}-workflow.xml").read_text(encoding="utf-8")

    def test_linked_items_status_with_type_uses_script(self):
        xml_ = self._wf("fr", "changeRequest")
        self.assertIn("fra-link-status.js", xml_)
        self.assertRegex(xml_, r'fra-link-status\.js"/><param name="rule" value="[^"]*type=action')

    def test_value_if_empty_uses_script(self):
        self.assertIn("fra-set-if-empty.js", self._wf("fr", "equipmentRequirement"))

    def test_required_at_submission_is_injected(self):
        xml_ = self._wf("fr", "function")
        submit = xml_.split('<action id="submit"')[1].split("</action>")[0]
        for f in ("functionLevel", "functionType", "discipline"):
            self.assertIn(f'<field name="{f}"/>', submit)

    def test_document_cascade_groups_items_by_type_and_status(self):
        doc = (self.out / "fr/.polarion/documents/workflow/systemSpec-workflow.xml").read_text(encoding="utf-8")
        self.assertRegex(doc, r'InvokeAction.*actionId" value="submit".*query" value="type:\([^)]*systemRequirement[^)]*\) AND status:\(')
        self.assertRegex(doc, r'InvokeAction.*actionId" value="approve"')

    def test_pseudo_roles_are_never_emitted_as_role_conditions(self):
        for f in (self.out / "fr" / ".polarion").rglob("*-workflow.xml"):
            dom = xml.dom.minidom.parse(str(f))
            for p in dom.getElementsByTagName("param"):
                if p.getAttribute("name") == "roles":
                    for r in p.getAttribute("value").split(","):
                        self.assertNotIn(r.strip(), ("anyProjectMember", "documentOwner"), f.name)
        self.assertIn("fra-document-owner.js",
                      (self.out / "fr/.polarion/documents/workflow/systemSpec-workflow.xml").read_text(encoding="utf-8"))

    def test_signatures_emitted_where_declared(self):
        wf = self.model.workflows["wfChangeRequest"]
        declared = sum(1 for tr in wf["transitions"] if tr.get("signature"))
        self.assertGreater(declared, 0)
        self.assertEqual(self._wf("fr", "changeRequest").count("<signatures>"), declared)
        self.assertEqual(self._wf("fr", "systemRequirement").count("<signatures>"), 0,
                         "wfRequirement : signature portée par le LiveDoc (ADR-30)")

    def test_english_configuration_uses_english_labels(self):
        en = self._wf("en", "changeRequest")
        self.assertIn('name="Approve (lightweight CCB, class II)"', en)
        self.assertNotIn("Approuver", en)
        for f in (self.out / "en" / ".polarion" / "tracker" / "workflow").glob("*-workflow.xml"):
            dom = xml.dom.minidom.parse(str(f))
            for a in dom.getElementsByTagName("action"):
                self.assertNotRegex(a.getAttribute("name"), r"[éèêà]", f"{f.name}: {a.getAttribute('name')}")

    def test_manifest_lists_every_script_used(self):
        manifest = (self.out / "fr" / "SIGNATURES_ET_SCRIPTS.md").read_text(encoding="utf-8")
        used = set()
        for f in (self.out / "fr" / ".polarion").rglob("*-workflow.xml"):
            for m_ in __import__("re").findall(r"fra-[a-z-]+\.js", f.read_text(encoding="utf-8")):
                used.add(m_)
        self.assertGreaterEqual(len(used), 15)
        for script in used:
            self.assertIn(f"`{script}`", manifest)


if __name__ == "__main__":
    unittest.main()
