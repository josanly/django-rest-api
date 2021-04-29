from django.test import TestCase
from django_rest_api.core.models import Analysis

# Create your tests here.
class AnalysisTestCase(TestCase):
    def setUp(self):
        Analysis.objects.create(name="analysis-test")

    def test_analysis_created_date(self):
        """Analysis nimals that can speak are correctly identified"""
        analysis = Analysis.objects.get(name="analysis-test")
        self.assertEqual(analysis.name, 'analysis-test')
