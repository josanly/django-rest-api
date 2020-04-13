from django.contrib.auth.models import User, Group
from rest_framework import serializers
from django_rest_api.core.models import Analysis

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']


class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']


# Serializer based on Django framework
# class AnalysisSerializer(serializers.Serializer):
#     id      = serializers.IntegerField(read_only=True)
#     name    = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     sample  = serializers.CharField(required=True, allow_blank=False, max_length=100)
#     comment = serializers.CharField(style={'base_template': 'textarea.html'})
    

#     def create(self, validated_data):
#         """
#         Create and return a new `Analysis` instance, given the validated data.
#         """
#         return Analysis.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Analysis` instance, given the validated data.
#         """
#         instance.name    = validated_data.get('name', instance.name)
#         instance.sample  = validated_data.get('sample', instance.sample)
#         instance.comment = validated_data.get('comment', instance.comment)
#         instance.save()
#         return instance


# REST framework includes both Serializer classes, and ModelSerializer classes.
# refactoring using ModelSerializer
# from this class you can print its representation to obtain the same as before
# $ python manage.py shell
# >>>from django_rest_api.core.serializers import AnalysisSerializer
# >>>serializer = AnalysisSerializer()
# >>>print(repr(serializer))
# AnalysisSerializer():
#     id = IntegerField(label='ID', read_only=True)
#     name = CharField(max_length=100, required=False)
#     comment = CharField(style={'base_template': 'textarea.html'})
#     sample = CharField(max_length=100, required=False)

# Serializer based on Django REST framework => more concise
class AnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Analysis
        fields = ['id', 'name', 'comment', 'sample']