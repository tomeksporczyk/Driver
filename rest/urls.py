from django.urls import include, path
from rest_framework import routers

from rest.views import AdviceSerializerView, TagSerializerView, UserSerializerView, \
    AnswerSerializerView, QuestionSerializerView

router = routers.DefaultRouter()
router.register('testquestion', QuestionSerializerView)
router.register('testanswer', AnswerSerializerView)
# router.register('quiz', QuizSerializerView, basename='quiz')
router.register('advice', AdviceSerializerView)
router.register('tag', TagSerializerView)
router.register('user', UserSerializerView)

urlpatterns = [
    path('rest/', include(router.urls)),
    path('api-auth', include('rest_framework.urls')),
    # path('quiz/', QuizSerializerView.as_view())
]