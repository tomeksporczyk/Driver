from collections import namedtuple

from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView

from driver.models import TestQuestion, Advice, Tag, TestAnswer
from rest.serializers import QuestionSerializer, AdviceSerializer, TagSerializer, UserSerializer, AnswerSerializer


class QuestionSerializerView(viewsets.ModelViewSet):
    queryset = TestQuestion.objects.all()
    serializer_class = QuestionSerializer


class AnswerSerializerView(viewsets.ModelViewSet):
    queryset = TestAnswer.objects.all()
    serializer_class = AnswerSerializer
#
# QandA = namedtuple('QuestionAnswer', ('question', 'answer'))
#
#
# class QuizSerializerView(viewsets.ViewSet):
#     def list(self, request):
#         q_and_a = QandA(question=TestQuestion.objects.all(),
#                         answer=TestAnswer.objects.all())
#         serializer = QuestionAnswerSerializer(q_and_a)
#         return Response(serializer.data)

        # questionanswer = QuestionAnswerSerializer
        # question = TestQuestion.objects.all()
        # question_serializer = QuestionSerializer(question, many=True)
        # answer = TestAnswer.objects.all()
        # answer_serializer = AnswerSerializer(answer, many=True)
        #
        # return Response({'question': question_serializer.data,
        #                  'answer': answer_serializer.data})


class AdviceSerializerView(viewsets.ModelViewSet):
    queryset = Advice.objects.all()
    serializer_class = AdviceSerializer


class TagSerializerView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer


class UserSerializerView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

