import os
import unittest
import unittest.mock

from django.conf import settings
from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404
from django.test import TestCase, Client

# Create your tests here.
from django.urls import reverse

from driver.models import Advice
from driver.tests_tools import create_image, create_advice, create_user


class ToolsTestCase(TestCase):

    def test_create_image(self):
        image = create_image('test.jpg', '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg')
        self.assertEqual(image.name, 'test.jpg')

    def setUp(self):
        self.file = create_image('test_image.jpg',
                                 '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg')
        self.user = create_user()

    def test_weeks_advice(self):
        create_advice('weeks', self.file,)
        advice = Advice.objects.get(weeks_advice=True)
        self.assertEqual(advice.title, "Week's advice")

    def test_normal_advice(self):
        create_advice('normal', self.file,)
        advice = Advice.objects.get(lead='Normal lead')
        self.assertEqual(advice.title, "Normal advice")

    def test_passed_advice(self):
        create_advice('passed', self.file, self.user)
        advice = Advice.objects.get(passed__username=self.user.username)
        self.assertEqual(advice.title, "Passed advice")


class HomeAdvicelessTestCase(TestCase):
    """
    get the home page with no Advice objects created
    """
    def test_empty_advice_table_status_handling(self):
        """
        :return: response 404 if no Advice objects were created
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)


class HomeTestCase(TestCase):

    def setUp(self):
        self.image = create_image('test_image.jpg',
                                  '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg')
        self.user = create_user()
        self.weeks = create_advice('weeks', self.image)
        self.normal = create_advice('normal', self.image)
        self.passed = create_advice('passed', self.image, self.user)

    def tearDown(self):
        os.remove(self.weeks.media.path)
        os.remove(self.normal.media.path)
        os.remove(self.passed.media.path)

    def test_home_status(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_home_displays_weeks_advice(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Week&#39;s advice")

    def test_home_displays_normal_advice(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Normal advice")

    def test_home_displays_passed_advice(self):
        response = self.client.get(reverse('home'))
        self.assertContains(response, "Passed advice")

    def test_home_advice_ordering(self):
        response = self.client.get(reverse('home'))
        query_set = Advice.objects.exclude(weeks_advice=True).order_by('-created_date')
        self.assertQuerysetEqual(response.context['advices_not_passed'], [repr(_) for _ in query_set])


if __name__ == "__main__":
    unittest.main()

