import unittest.mock

from django.contrib.auth.models import User
from django.core.files import File
from django.core.files.uploadedfile import SimpleUploadedFile

from driver.models import Tag, Advice


def create_tag(name):
    """
    :param name: string - a tag's name
    :return: creates a Tag object
    """
    return Tag.objects.create(name=name)


def create_image(file_name, dir):
    """
    :param file_name: string - name of the file
    dir: directory of the file
    :return: a file
    """
    file = SimpleUploadedFile(name=file_name,
                              content=open(dir, 'rb').read())
    return file


def create_advice(advice_type, file, user=None):
    """

    :param advice_type: sting = 'weeks' or 'normal' or 'passed
    :param file: file object = created with create_image function
    :param user: user instance = created with create_user function. Leave as None if not creating passed_advice
    :return: an instance of an Advice - week's advice, normal, or passed
    """
    if advice_type == 'weeks':
        tag = create_tag('weeks_advice')
        advice = Advice.objects.create(
            title="Week's advice",
            lead="Week's lead",
            article="Week's article",
            media=file,
            weeks_advice=True,
            )
        advice.tags.add(tag)
    elif advice_type == 'normal':
        tag = create_tag('normal_advice')
        advice = Advice.objects.create(
            title="Normal advice",
            lead="Normal lead",
            article="Normal article",
            media=file,
            weeks_advice=False,
        )
        advice.tags.add(tag)
        advice.save()
    elif advice_type == 'passed':
        tag = create_tag('passed_advice')
        advice = Advice.objects.create(
            title="Passed advice",
            lead="Passed lead",
            article="Passed article",
            media=file,
            weeks_advice=False,
            )
        advice.passed.add(user)
        advice.save()
        advice.tags.add(tag)
    else:
        pass
    return advice


def create_user():
    return User.objects.create_user(username='testuser', email='test@user.com', password='test')