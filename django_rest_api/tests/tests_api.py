from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_rest_api.core.models import Analysis

class AnalysisTests(APITestCase):
    def test_create_analysis(self):
        """
        Ensure we can create a new analysis object.
        """
        url = reverse('analyses')
        analysis_name = 'analysis-test'
        data = {'name': analysis_name}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Analysis.objects.count(), 1)
        self.assertEqual(Analysis.objects.get().name, analysis_name)