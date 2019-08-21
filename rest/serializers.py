
"""
todo: forum api, quiz api with posting both q and a
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from driver.models import TestQuestion, Advice, Tag, TestAnswer


class AnswerSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TestAnswer
        fields = '__all__'


class AdviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Advice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = TestQuestion
        fields = ['advice', 'question']


class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'is_staff', 'is_active', 'email']

