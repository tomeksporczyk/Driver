from django.urls import path

from forum.views import forum_topics_view, topic_threads_view, NewThreadView, AnswersView

urlpatterns = [
    path('forum', forum_topics_view, name='forum'),
    path('forum/<int:pk>', topic_threads_view, name='threads'),
    path('forum/<int:pk>/new-thread', NewThreadView.as_view(), name='new_thread'),
    path('forum/thread/<int:t_pk>', AnswersView.as_view(), name='thread'),
]
