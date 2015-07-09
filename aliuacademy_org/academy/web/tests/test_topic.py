# -*- encoding: utf-8 -*-
import pytest

from web.models import (
    Course,
    Department,
    Topic,
    University,
)


def _setup_get_next_prev():
    uni = University.objects.create_university('Exeter')
    dept = Department.objects.create_department(uni, 'exeter')
    course = Course.objects.create_course(dept, 1, 'economics')
    for counter in range(1, 6):
        print(counter)
        Topic.objects.create_topic(
            course=course,
            order=counter,
            file_path='/home/patrick/video_{}.mp4'.format(counter),
            file_type=Topic.VIDEO,
        )
    return Topic.objects.get(order=3)


@pytest.mark.django_db
def test_download_file_name():
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


@pytest.mark.django_db
def test_get_next():
    topic = _setup_get_next_prev()
    assert 4 == topic.get_next.order


@pytest.mark.django_db
def test_get_prev():
    topic = _setup_get_next_prev()
    assert 2 == topic.get_prev.order


@pytest.mark.django_db
def test_active_objects():
    topic = _setup_get_next_prev()
    qs = Topic.active_objects.all().order_by('order')
    assert [1, 2, 3, 4, 5] == [obj.order for obj in qs]
