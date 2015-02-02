# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import os

from web.service import (
    AcademyError,
    VideoReader,
    number_from_string,
)


class TestServiceVideoReader(TestCase):

    def setUp(self):
        self.folder = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'data',
            'media_root',
        )

    def test_init(self):
        VideoReader(self.folder)

    def test_read(self):
        VideoReader(self.folder).update()

    def test_number_from_string(self):
        result = number_from_string('abc123')
        assert 123 == result

    def test_number_from_string_except(self):
        with self.assertRaises(AcademyError):
            number_from_string('abc')

    def test_number_from_string_two_number(self):
        assert 456 == number_from_string('abc456xyz123red')
