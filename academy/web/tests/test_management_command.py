# -*- encoding: utf-8 -*-
import os

from django.test import TestCase

from web.management.commands import init_app_web


class TestCommand(TestCase):

    def test_init_app(self):
        """ Test the management command """
        # copied from 'web/tests/test_service_video_reader.py'
        folder = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'data',
            'media_root',
        )
        with self.settings(MEDIA_ROOT=folder):
            command = init_app_web.Command()
            command.handle()
