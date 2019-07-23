from django.contrib import admin

# Register your models here.
from driver.models import Advice, Tag, TestQuestion, TestAnswer, ForumTopic, ForumThread, ForumAnswer

admin.site.register(Advice)
admin.site.register(Tag)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
admin.site.register(ForumTopic)
admin.site.register(ForumThread)
admin.site.register(ForumAnswer)