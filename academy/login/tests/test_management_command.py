# -*- encoding: utf-8 -*-
from django.test import TestCase

from login.management.commands import demo_data_login


class TestCommand(TestCase):

    def test_command_demo_data_login(self):
        command = demo_data_login.Command()
        command.handle()
