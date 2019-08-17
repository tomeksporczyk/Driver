from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from django.urls import reverse_lazy
from django.views import View

from forum.forms import NewThreadForm, AnswerForm
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
            thread = form.save(commit=False)
            thread.topic = ForumTopic.objects.get(pk=pk)
            thread.created_by = request.user
            thread.save()
            return redirect(f'/forum/{pk}')


class AnswersView(View):
    def get(self, request, t_pk):
        form = AnswerForm().as_p()
        thread = get_object_or_404(ForumThread, pk=t_pk)
        answers_list = thread.forumanswer_set.all().order_by('-created_date_time')
        paginator = Paginator(answers_list, 5)
        page = request.GET.get('page')
        answers = paginator.get_page(page)
        context = {'thread': thread, 'answers': answers, 'form': form}
        return render(request, 'forum/forum_thread.html', context)

    def post(self, request, t_pk):
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.title = ForumThread.objects.get(pk=t_pk)
            answer.created_by = request.user
            answer.save()
            return self.get(request, t_pk)
        else:
            return self.get(request, t_pk)
