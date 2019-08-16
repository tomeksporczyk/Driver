from django.urls import path

from forum.views import forum_topics_view, topic_threads_view, NewThreadView

urlpatterns = [
    path('forum', forum_topics_view, name='forum'),
    path('forum/<int:pk>', topic_threads_view, name='threads'),
    path('forum/<int:pk>/new-thread', NewThreadView.as_view(), name='new_thread'),
]
