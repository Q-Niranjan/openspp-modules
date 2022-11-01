import logging

from odoo.tests import tagged
from odoo.tests.common import TransactionCase

_logger = logging.getLogger(__name__)


@tagged("post_install", "-at_install")
class EventPhoneSurveyTest(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(EventPhoneSurveyTest, cls).setUpClass()

        # Initial Setup of Variables
        cls.group_1 = cls.env["res.partner"].create(
            {
                "name": "Group 1",
                "is_registrant": True,
                "is_group": True,
            }
        )
        cls.phone_survey_1 = cls.env["spp.event.phone.survey"].create(
            {
                "summary": "Testing Visit",
                "description": "This visit is for testing only",
            }
        )
        cls.event_data_1 = cls.env["spp.event.data"].create(
            {
                "partner_id": cls.group_1.id,
                "model": "spp.event.phone.survey",
                "res_id": cls.phone_survey_1.id,
            }
        )

    def test_01_check_active_phone_survey(self):
        self.group_1._compute_active_phone_survey()
        self.assertEqual(
            self.group_1.active_phone_survey.id,
            self.event_data_1.id,
        )

    def test_02_check_name(self):
        phone_survey_create_date = self.group_1.active_phone_survey.create_date
        self.assertEqual(
            self.group_1.active_phone_survey.name,
            "Phone Survey - [%s]" % phone_survey_create_date,
        )

    def test_03_recheck_active_phone_survey_after_entering_new_visit(self):
        vals_phone = {
            "summary": "Testing Visit 2",
            "description": "This visit is for testing again",
        }
        phone_survey_2 = self.env["spp.event.phone.survey"].create(vals_phone)

        vals_event_data = {
            "partner_id": self.group_1.id,
            "model": "spp.event.phone.survey",
            "res_id": phone_survey_2.id,
        }
        event_data_2 = self.env["spp.event.data"].create(vals_event_data)
        self.group_1._compute_active_phone_survey()
        self.assertEqual(
            self.group_1.active_phone_survey.id,
            event_data_2.id,
        )