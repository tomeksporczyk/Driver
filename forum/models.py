from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class ForumTopic(models.Model):
    name = models.CharField(max_length=512, unique=True)

    def __str__(self):
        return self.name


class ForumThread(models.Model):
    topic = models.ForeignKey(ForumTopic, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    text = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    thread_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class ForumAnswer(models.Model):
    title = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    text = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
