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


def create_weeks_advice(file_name, dir, tag_name):
    """
    todo: create one create_advice function for all advice types
    :param file_name: string - name of media file to upload
    :param dir: string - directory of the file
    :param tag_name: string - name of the tag to be created
    :return: creates Advice object with weeks_advice set to True
    """
    tag = create_tag(tag_name)
    advice = Advice.objects.create(
                        title="Week's advice",
                        lead="Week's lead",
                        article="Week's article",
                        media=create_image(file_name, dir),
                        weeks_advice=True,
                        )
    advice.tags.add(tag)
    return advice


def create_advice(file_name, dir, tag_name):
    """
    :param file_name: string - name of media file to upload
    :param dir: string - directory of the file
    :param tag_name: string - name of the tag to be created
    :return: creates Advice object
    """
    tag = create_tag(tag_name)
    advice = Advice.objects.create(
        title="Normal advice",
        lead="Normal lead",
        article="Normal article",
        media=create_image(file_name, dir),
        weeks_advice=False,
    )
    advice.tags.add(tag)
    advice.save()
    return advice


def create_passed_advice(user, file_name, dir, tag_name):
    """
    :param user: user instance
    :param file_name: string - name of media file to upload
    :param dir: string - directory of the file
    :param tag_name: string - name of the tag to be created
    :return: creates Advice object with passed field including the user
    """
    tag = create_tag(tag_name)
    advice = Advice.objects.create(
        title="Passed advice",
        lead="Passed lead",
        article="Passed article",
        media=create_image(file_name, dir),
        weeks_advice=False,
    )
    advice.passed.add(user)
    advice.save()
    advice.tags.add(tag)
    return advice


def create_user():
    return User.objects.create_user(username='testuser', email='test@user.com', password='test')