from django.test import TestCase

import os

from aliu.service import FtpReader


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
