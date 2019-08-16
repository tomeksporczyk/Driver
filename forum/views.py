
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from forum.forms import NewThreadForm
from forum.models import ForumTopic, ForumThread


def forum_topics_view(request):
    topics = ForumTopic.objects.all()
    return render(request, 'forum/forum_topics.html', context={'topics': topics})


def topic_threads_view(request, pk):
    threads = ForumThread.objects.filter(topic=pk)
    return render(request, 'forum/forum_threads.html', context={'threads': threads, 'pk': pk})


class NewThreadView(View):
    def get(self, request, pk):
        form = NewThreadForm().as_p()
        return render(request, 'uni_form.html', context={'form': form, 'submit': 'Publikuj'})

    def post(self, request, pk):
        form = NewThreadForm(request.POST)
        if form.is_valid():
            # print(form.cleaned_data.get('topic'))
            # print(form.cleaned_data.get('created_by'))
            # print(form.cleaned_data.get('title'))
            # print(form.cleaned_data.get('text'))
            # print(form.cleaned_data.get('created_date_time'))
            thread = form.save(commit=False)
            thread.topic = ForumTopic.objects.get(pk=pk)
            thread.created_by = request.user
            thread.save()
            return redirect(f'/forum/{pk}')


