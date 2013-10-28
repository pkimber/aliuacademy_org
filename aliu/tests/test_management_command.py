from django.test import TestCase

from aliu.management.commands import demo_data_aliu
from aliu.management.commands import init_app_aliu


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        command = demo_data_aliu.Command()
        command.handle()

    def test_init_app(self):
        """ Test the management command """
        command = init_app_aliu.Command()
        command.handle()
