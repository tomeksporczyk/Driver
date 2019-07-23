from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.utils import timezone


class Advice(models.Model):
    title = models.CharField(max_length=256)
    lead = models.CharField(max_length=1280)
    article = models.TextField()
    created_date = models.DateField(editable=False)
    tags = models.ManyToManyField('Tag')
    media = models.FileField(upload_to='advice/miedia/')

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=64)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=False)

    def save(self, *args, **kwargs):
        if self.like:
            self.dislike = False
        else:
            self.dislike = True
        return super().save(*args, **kwargs)

    def update(self, *args, **kwargs):
        if self.like:
            self.dislike = False
        else:
            self.dislike = True
        if self.dislike:
            self.like = False
        else:
            self.like = True
        return super().update(*args, **kwargs)


class TestQuestion(models.Model):
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    question = models.CharField(max_length=512)


class TestAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=512)
    is_truth = models.BooleanField(default=False)


class ForumTopic(models.Model):
    name = models.CharField(max_length=512)


class ForumThread(models.Model):
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    thread_closed = models.BooleanField(default=False)


class ForumAnswer(models.Model):
    title = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    text = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)