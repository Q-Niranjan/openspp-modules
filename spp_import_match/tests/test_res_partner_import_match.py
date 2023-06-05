from os import path

from odoo.tests import TransactionCase

PATH = path.join(path.dirname(__file__), "import_data", "%s.csv")
OPTIONS = {
    "headers": True,
    "quoting": '"',
    "separator": ",",
}


class TestResPartnerImportMatch(TransactionCase):
    def setUp(self):
        super().setUp()
        self._test_hh = self.env["res.partner"].create(
            {
                "name": "Renaud",
                "is_registrant": True,
                "is_group": True,
                "email": "renaud@gmail.com",
            }
        )
        self._test_applicant = self.env["res.partner"].create(
            {
                "name": "Rufino Renaud",
                "family_name": "Renaud",
                "given_name": "Rufino",
                "is_group": False,
                "is_registrant": True,
                "phone": "+639266716911",
                "email": "rufinorenaud12@gmail.com",
            }
        )

    def _base_import_record(self, res_model, file_name):
        with open(PATH % file_name) as demo_file:
            return self.env["base_import.import"].create(
                {
                    "res_model": res_model,
                    "file": demo_file.read(),
                    "file_name": "%s.csv" % file_name,
                    "file_type": "csv",
                }
            )

    def create_matching_given_family_name(self):
        res_partner = self.env["ir.model"].search([("model", "=", "res.partner")])
        vals = {"name": res_partner.id}
        import_match = self.env["spp.import.match"].create(vals)
        given_name_field = self.env["ir.model.fields"].search(
            [("name", "=", "given_name")]
        )

        self.env["spp.import.match.fields"].create(
            {"field_id": given_name_field.id, "match_id": import_match.id}
        )

        family_name_field = self.env["ir.model.fields"].search(
            [("name", "=", "given_name")]
        )

        self.env["spp.import.match.fields"].create(
            {"field_id": family_name_field.id, "match_id": import_match.id}
        )

        return import_match

    def create_matching_name(self):
        res_partner = self.env["ir.model"].search([("model", "=", "res.partner")])
        vals = {"name": res_partner.id}
        import_match = self.env["spp.import.match"].create(vals)
        name_field = self.env["ir.model.fields"].search([("name", "=", "name")])

        self.env["spp.import.match.fields"].create(
            {"field_id": name_field.id, "match_id": import_match.id}
        )

        return import_match

    def test_01_res_partner_name(self):
        """Change email based on Name."""
        self.create_matching_given_family_name()
        record = self._base_import_record("res.partner", "res_partner_name")
        record.execute_import(["id", "given_name", "family_name", "email"], [], OPTIONS)
        self._test_applicant.env.cache.invalidate()
        self.assertEqual(self._test_applicant.email, "rufinorenaud@gmail.com")

    def test_02_res_partner_group_name(self):
        """Change email based on Name."""
        self.create_matching_name()
        record = self._base_import_record("res.partner", "res_partner_group_name")
        record.execute_import(["id", "name", "email"], [], OPTIONS)
        self._test_hh.env.cache.invalidate()
        self.assertEqual(self._test_hh.email, "renaudhh@gmail.com")