from django.contrib import admin

# Register your models here.
from forum.models import ForumTopic, ForumThread, ForumAnswer

admin.site.register(ForumTopic)
admin.site.register(ForumThread)
admin.site.register(ForumAnswer)