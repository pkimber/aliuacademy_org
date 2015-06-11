# -*- encoding: utf-8 -*-
from django.test import TestCase

from web.management.commands import init_app_web


class TestCommand(TestCase):

    def test_init_app(self):
        """ Test the management command """
        command = init_app_web.Command()
        command.handle()
