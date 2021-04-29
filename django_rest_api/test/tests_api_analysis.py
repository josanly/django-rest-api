from django.contrib.auth.models import User
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django_rest_api.core.models import Analysis
from django_rest_api import urls

class AnalysisTests(APITestCase):
    def test_create_analysis(self):
        """
        Ensure we can create a new analysis object.
        """
        # see https://www.django-rest-framework.org/api-guide/routers/#defaultrouter
        # to know the url name
        url = reverse('analyses-list')
        analysis_name = 'analysis-test'
        data = {'name': analysis_name}

        # force auth
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

        response = self.client.post(url, data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Analysis.objects.count(), 1)
        self.assertEqual(Analysis.objects.get().name, analysis_name)

    def test_get_analysis(self):
        """
        Ensure we retrieve list of analysis objects.
        """

        # create an anlysis
        Analysis.objects.create(name='analysis-test')

        url = reverse('analyses-list')

        # force auth
        user = User.objects.create_user('username', 'Pas$w0rd')
        self.client.force_authenticate(user)

        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)
        self.assertEqual(len(response.data['results']), 1)
        self.assertEqual(response.data['results'][0]['name'], 'analysis-test')

        response = self.client.get('{}{}/'.format(url, 1), format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'analysis-test')
        self.assertEqual(response.data['id'], 1)
