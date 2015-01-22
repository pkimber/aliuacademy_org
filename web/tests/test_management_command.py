# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

from web.management.commands import demo_data_web
from web.management.commands import init_app_web


class TestCommand(TestCase):

    def test_demo_data(self):
        """ Test the management command """
        command = demo_data_web.Command()
        command.handle()

    def test_init_app(self):
        """ Test the management command """
        command = init_app_web.Command()
        command.handle()
