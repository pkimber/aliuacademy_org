# -*- encoding: utf-8 -*-
from django.test import TestCase

from web.models import (
    Course,
    Department,
    Topic,
    University,
)


class TestTopic(TestCase):

    def test_download_file_name(self):
        uni = University.objects.create_university('Exeter')
        dept = Department.objects.create_department(uni, 'exeter')
        course = Course.objects.create_course(dept, 1, 'economics')
        topic = Topic.objects.create_topic(
            course=course,
            order=1,
            file_path='/home/patrick/video.mp4',
            file_type=Topic.VIDEO,
        )
        assert 'video.mp4' == topic.download_file_name()
