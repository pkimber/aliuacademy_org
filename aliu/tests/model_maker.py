from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from aliu.models import (
    Course,
    Department,
    Topic,
    University,
)


def make_course(department, order, folder_name, **kwargs):
    defaults = dict(
        department=department,
        order=order,
        name=folder_name,
        folder_name=folder_name,
    )
    defaults.update(kwargs)
    return clean_and_save(Course(**defaults))


def make_department(university, folder_name, **kwargs):
    defaults = dict(
        university=university,
        name=folder_name,
        folder_name=folder_name,
    )
    defaults.update(kwargs)
    return clean_and_save(Department(**defaults))


def make_topic(course, order, file_name, **kwargs):
    defaults = dict(
        order=order,
        name=file_name,
        video=file_name,
        course=course,
    )
    defaults.update(kwargs)
    return clean_and_save(Topic(**defaults))


def make_university(folder_name, **kwargs):
    defaults = dict(
        slug=slugify(unicode(folder_name)),
        name=folder_name,
        folder_name=folder_name,
    )
    defaults.update(kwargs)
    return clean_and_save(University(**defaults))
