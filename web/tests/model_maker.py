# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""Create model instances in the database."""
import os

from django.utils.text import slugify

from base.tests.model_maker import clean_and_save

from web.models import (
    Course,
    Department,
    Topic,
    University,
)


def make_course(department, order, folder_name, **kwargs):
    """Create a 'Course' in the database and return it."""
    defaults = dict(
        department=department,
        order=order,
        name=folder_name,
        folder_name=folder_name,
    )
    defaults.update(kwargs)
    return clean_and_save(Course(**defaults))


def make_department(university, folder_name, **kwargs):
    """Create a 'Department' in the database and return it."""
    defaults = dict(
        university=university,
        name=folder_name,
        folder_name=folder_name,
    )
    defaults.update(kwargs)
    return clean_and_save(Department(**defaults))


def make_topic(course, order, file_path, **kwargs):
    """Create a 'Topic' in the database and return it."""
    name = os.path.basename(file_path)
    name, _ = os.path.splitext(name)
    defaults = dict(
        order=order,
        name=name,
        video=file_path,
        course=course,
    )
    defaults.update(kwargs)
    return clean_and_save(Topic(**defaults))


def make_university(folder_name, **kwargs):
    """Create a 'University' in the database and return it."""
    defaults = dict(
        slug=slugify(folder_name),
        name=folder_name,
        folder_name=folder_name,
    )
    defaults.update(kwargs)
    return clean_and_save(University(**defaults))
