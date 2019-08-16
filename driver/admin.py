from django.contrib import admin

# Register your models here.
from driver.models import Advice, Tag, TestQuestion, TestAnswer

admin.site.register(Advice)
admin.site.register(Tag)
admin.site.register(TestQuestion)
admin.site.register(TestAnswer)
