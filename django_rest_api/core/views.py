from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.views.generic import TemplateView
from rest_framework import viewsets
from rest_framework import permissions
from django_rest_api.core.serializers import UserSerializer, GroupSerializer, AnalysisSerializer
from django_rest_api.core.models import Analysis


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


class AnalysisViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows analyses to be viewed or edited.
    """
    queryset = Analysis.objects.all()
    serializer_class = AnalysisSerializer
    permission_classes = [permissions.IsAuthenticated]