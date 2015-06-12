# -*- encoding: utf-8 -*-
"""Service class."""

import os
import re

from .models import (
    Course,
    Department,
    Topic,
    University,
)


class AcademyError(Exception):

    """Exception class for the Aliu Academy app."""

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr('%s, %s' % (self.__class__.__name__, self.value))


def number_from_string(text):
    """Return the first number from a string."""
    items = re.findall(r'\d+', text)
    if items:
        return int(items[0])
    else:
        raise AcademyError("'{}' does not contain a number".format(text))


class VideoReader(object):
    """Walk the file system to find videos and put into the course."""

    def __init__(self, folder):
        """Initialise with 'settings.MEDIA_ROOT'."""
        self.folder = folder

    def _read_courses(self, university, department):
        folder = os.path.join(
            self.folder,
            university,
            department,
        )
        order = 0
        folders = os.listdir(folder)
        for course in folders:
            path = os.path.join(folder, course)
            if os.path.isdir(path):
                order = order + 1
                print('Course: {}'.format(course))
                Course.objects.update_course(
                    university, department, order, course
                )
                self._read_topics(university, department, course)

    def _read_departments(self, university):
        folder = os.path.join(
            self.folder,
            university,
        )
        folders = os.listdir(folder)
        for department in folders:
            path = os.path.join(folder, department)
            if os.path.isdir(path):
                print('Department: {}'.format(department))
                Department.objects.update_department(university, department)
                self._read_courses(university, department)

    def _read_topics(self, university, department, course):
        folder = os.path.join(
            self.folder,
            university,
            department,
            course,
        )
        order = 0
        files = os.listdir(folder)
        files.sort()
        for topic in files:
            path = os.path.join(folder, topic)
            if os.path.isfile(path):
                order = order + 1
                print('Topic: {}'.format(topic))
                Topic.objects.update_topic(
                    university,
                    department,
                    course,
                    number_from_string(topic),
                    os.path.join(
                        university,
                        department,
                        course,
                        topic,
                    ),
                    topic
                )

    def _read_universities(self):
        folder = os.path.join(
            self.folder,
        )
        folders = os.listdir(folder)
        for university in folders:
            path = os.path.join(folder, university)
            if os.path.isdir(path):
                print('University: {}'.format(university))
                University.objects.update_university(university)
                self._read_departments(university)

    def update(self):
        """Update the database based on the folder structure."""
        self._read_universities()
