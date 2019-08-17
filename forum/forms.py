from django import forms

from forum.models import ForumThread, ForumAnswer


class NewThreadForm(forms.ModelForm):

    class Meta:
        model = ForumThread
        fields = ['title', 'text']


class AnswerForm(forms.ModelForm):

    class Meta:
        model = ForumAnswer
        fields = ['text']