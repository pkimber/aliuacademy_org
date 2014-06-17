# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.test import TestCase

import os

from aliu.service import (
    AcademyError,
    FtpReader,
    number_from_string,
)


class TestServiceFtpReader(TestCase):

    def setUp(self):
        self.folder = os.path.join(
            os.path.dirname(os.path.realpath(__file__)),
            'data',
            'ftp_static_dir',
        )

    def test_init(self):
        FtpReader(self.folder)

    def test_read(self):
        FtpReader(self.folder).update()

    def test_number_from_string(self):
        result = number_from_string('abc123')
        self.assertEquals(123, result)

    def test_number_from_string_except(self):
        self.assertRaises(AcademyError, number_from_string, 'abc')

    def test_number_from_string_two_number(self):
        result = number_from_string('abc456xyz123red')
        self.assertEquals(456, result)
