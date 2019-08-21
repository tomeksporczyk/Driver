import unittest
import unittest.mock

from django.contrib import auth
from django.test import TestCase, Client

# Create your tests here.
from driver.models import Advice, Tag
from driver.tests_tools import create_image, create_weeks_advice, create_advice, create_passed_advice


class ToolsTestCase(TestCase):

    def test_create_image(self):
        image = create_image('test.jpg', '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg')
        self.assertEqual(image.name, 'test.jpg')

    def test_weeks_advice(self):
        file_name = 'test_week_advice.jpg'
        dir = '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg'
        tag_name = 'weeks advice tag'
        advice = create_weeks_advice(file_name, dir, tag_name)
        self.assertEqual(advice.title, "Week's advice")

    def test_normal_advice(self):
        file_name = 'test_normal_advice.jpg'
        dir = '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg'
        tag_name = 'normal advice tag'
        advice = create_advice(file_name, dir, tag_name)
        self.assertEqual(advice.title, "Normal advice")

    def test_passed_advice(self):
        '''
        todo: user = authenticated user
        '''
        user = auth.get_user(self.)
        file_name = 'test_passed_advice.jpg'
        dir = '/home/tomek/PycharmProjects/Driver/media/advice/harold.jpg'
        tag_name = 'passed advice tag'
        advice = create_passed_advice(user, file_name, dir, tag_name)
        self.assertEqual(advice.title, "Passed advice")


if __name__ == "__main__":
    unittest.main()

