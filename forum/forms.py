from django import forms

from forum.models import ForumThread


class NewThreadForm(forms.ModelForm):

    class Meta:
        model = ForumThread
        fields = ['title', 'text']
