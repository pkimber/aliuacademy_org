# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase

import os

from web.models import Topic
from web.tests.model_maker import (
    make_course,
    make_department,
    make_topic,
    make_university,
)


class TestTopic(TestCase):

    def test_download_file_name(self):
        uni = make_university('Exeter')
        dept = make_department(uni, 'exeter')
        course = make_course(dept, 1, 'economics')
        topic = make_topic(
            course=course,
            order=1,
            file_path='/home/patrick/video.mp4',
        )
        self.assertEquals('video.mp4', topic.download_file_name())
