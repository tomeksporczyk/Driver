import magic
from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils import timezone
from django.utils.text import slugify


class Advice(models.Model):
    title = models.CharField(max_length=256)
    lead = models.CharField(max_length=1280)
    article = models.TextField()
    created_date = models.DateField(editable=False)
    tags = models.ManyToManyField('Tag')
    media = models.FileField(upload_to='advice/')
    media_type = models.CharField(max_length=50, editable=False)
    weeks_advice = models.BooleanField(default=False)
    passed = models.ManyToManyField(User, blank=True)
    slug = models.SlugField(unique=True, editable=False)
    likes = models.IntegerField(default=0, editable=False)

    def __str__(self):
        return self.title

    def _get_media_type(self):
        return magic.from_buffer(self.media.read(), mime=True)

    def _get_unique_slug(self):
        slug = slugify(self.title)
        unique_slug = slug
        number = 1
        while Advice.objects.filter(slug=unique_slug).exists():
            unique_slug = f'{unique_slug}-{number}'
            number += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.id:
            self.created_date = timezone.now()
            self.media_type = self._get_media_type()
        if not self.slug:
            self.slug = self._get_unique_slug()

        return super().save(*args, **kwargs)


class Tag(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    like = models.BooleanField(default=False)
    dislike = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.like:
            self.dislike = False
        else:
            self.dislike = True
        return super().save(*args, **kwargs)


class TestQuestion(models.Model):
    advice = models.ForeignKey(Advice, on_delete=models.CASCADE)
    question = models.CharField(max_length=512)

    def __str__(self):
        return self.question


class TestAnswer(models.Model):
    question = models.ForeignKey(TestQuestion, on_delete=models.CASCADE)
    answer = models.CharField(max_length=512)
    is_truth = models.BooleanField(default=False)
    points = models.IntegerField(default=0)

    def save(self, *args, **kwargs):
        if self.is_truth is True and self.points < 1:
            self.points = 1
        return super().save(*args, **kwargs)


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


class ForumAnswer(models.Model):
    title = models.ForeignKey(ForumThread, on_delete=models.CASCADE)
    text = models.TextField()
    created_date_time = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)


class Score(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    score = models.IntegerField(default=0)


@receiver(post_save, sender=User)
def create_user_score(sender, instance, created, **kwargs):
    if created:
        Score.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_score(sender, instance, **kwargs):
    instance.score.save()