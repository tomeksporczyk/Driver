import unittest
import unittest.mock

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404
from django.test import TestCase, Client

# Create your tests here.
from driver.models import Advice
from driver.tests_tools import create_image, create_weeks_advice, create_advice, create_passed_advice, create_user


class ToolsTestCase(TestCase):

    def test_create_image(self):
        image = create_image('test.jpg', '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg')
        self.assertEqual(image.name, 'test.jpg')

    def test_weeks_advice(self):
        file_name = 'test_week_advice.jpg'
        dir = '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg'
        tag_name = 'weeks advice tag'
        create_weeks_advice(file_name, dir, tag_name)
        advice = Advice.objects.get(weeks_advice=True)
        self.assertEqual(advice.title, "Week's advice")

    def test_normal_advice(self):
        file_name = 'test_normal_advice.jpg'
        dir = '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg'
        tag_name = 'normal advice tag'
        create_advice(file_name, dir, tag_name)
        advice = Advice.objects.get(lead='Normal lead')
        self.assertEqual(advice.title, "Normal advice")

    def test_create_user(self):
        create_user()
        user = User.objects.first()
        self.assertEqual(user.username, 'testuser')

    def test_passed_advice(self):
        user = create_user()
        file_name = 'test_passed_advice.jpg'
        dir = '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg'
        tag_name = 'passed advice tag'
        create_passed_advice(user, file_name, dir, tag_name)
        advice = Advice.objects.get(passed__username=user.username)
        self.assertEqual(advice.title, "Passed advice")


class HomeTestCase(TestCase):

    def test_empty_advice_table_status_handling(self):
        """
        :return: response 404 if no Advice objects were created
        """
        response = self.client.get('/')
        self.assertEqual(response.status_code, 404)

    def setUp(self):
        create_image()

if __name__ == "__main__":
    unittest.main()

