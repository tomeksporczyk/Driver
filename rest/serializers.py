'''
todo: REST API
'''
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.relations import PrimaryKeyRelatedField

from driver.models import TestQuestion, Advice, Tag, TestAnswer


class AnswerSerializer(PrimaryKeyRelatedField, serializers.HyperlinkedModelSerializer):

    class Meta:
        model = TestAnswer
        fields = '__all__'


class AdviceSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Advice
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    answers = AnswerSerializer(many=True, queryset=TestAnswer.objects.all())

    class Meta:
        model = TestQuestion
        fields = ['advice', 'question', 'answers']

    def create(self, validated_data):
        answers_data = validated_data.pop('answers')
        question = TestQuestion.objects.create(**validated_data)
        for answer_data in answers_data:
            TestAnswer.objects.create(question=question, **answer_data)
        return question

# class QuestionAnswerSerializer(serializers.Serializer):
#     question = QuestionSerializer(many=True)
#     answer = AnswerSerializer(many=True)





class TagSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tag
        fields = '__all__'


class UserSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'is_staff', 'is_active', 'email']
