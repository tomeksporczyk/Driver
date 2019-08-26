import unittest
import unittest.mock

from django.contrib import auth
from django.contrib.auth.models import User
from django.http import Http404
from django.test import TestCase, Client

# Create your tests here.
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


# class HomeTestCase(TestCase):
#
#     def test_empty_advice_table_status_handling(self):
#         """
#         :return: response 404 if no Advice objects were created
#         """
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 404)
#
#     def setUp(self):
#         self.image = create_image('test_image.jpg',
#                      '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg')
#         self.user = create_user()
#         create_advice('weeks', self.image)
#         create_advice('normal', self.image)
#         create_advice('passed', self.image, self.user)



if __name__ == "__main__":
    unittest.main()

