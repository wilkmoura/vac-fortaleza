from datetime import datetime, timedelta
from django.test import TestCase
from django.db.models import Count
from schedule.scripts import get_schedules as script
from schedule.models import Spreadsheet


class ScriptTests(TestCase):
    def setUp(self):
        self.root_xml = script.get_root_spreadsheet()
        limit_date = (datetime.now() - timedelta(days=7)).date()
        self.entries = script.get_xml_entry_element(self.root_xml, limit_date)

    def test_get_root_xml(self):
        self.assertTrue(self.root_xml)

    def test_entries(self):
        self.assertGreaterEqual(len(list(self.entries)), 1)

    def test_save_spreadsheets(self):
        QTD_TO_SAVE = 10
        script.save_spreadsheets(list(self.entries)[:QTD_TO_SAVE])
        self.assertEqual(Spreadsheet.objects.count(), QTD_TO_SAVE)

    def test_processing(self):
        script.save_spreadsheets(self.entries)
        for spread in Spreadsheet.objects.all():
            script.process_spreadsheet(spread, 5)
