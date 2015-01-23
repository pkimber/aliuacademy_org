# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

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


def _update_course(university, department, order, course):
    univ = University.objects.get(folder_name=university)
    dept = Department.objects.get(university=univ, folder_name=department)
    print('Course: {}'.format(course))
    try:
        Course.objects.get(
            department=dept,
            folder_name=course
        )
    except Course.DoesNotExist:
        Course.objects.create_course(
            department=dept,
            order=order,
            folder_name=course,
        )


def _update_topic(university, department, course, order, path, topic):
    univ = University.objects.get(folder_name=university)
    dept = Department.objects.get(university=univ, folder_name=department)
    cour = Course.objects.get(department=dept, folder_name=course)
    print('Topic: {}'.format(topic))
    try:
        Topic.objects.get(
            course=cour,
            video=path,
        )
    except Topic.DoesNotExist:
        Topic.objects.create_topic(
            course=cour,
            order=order,
            file_path=path,
        )


def _update_department(university, department):
    uni = University.objects.get(folder_name=university)
    print('Department: {}'.format(department))
    try:
        Department.objects.get(
            university=uni,
            folder_name=department
        )
    except Department.DoesNotExist:
        Department.objects.create_department(
            university=uni,
            folder_name=department,
        )


def _update_university(university):
    print('University: {}'.format(university))
    try:
        University.objects.get(folder_name=university)
    except University.DoesNotExist:
        University.objects.create_university(folder_name=university)


class FtpReader(object):

    """
    Aliu will upload videos via FTP.

    Read the folder structure and update the database to reflect it.

    """

    def __init__(self, ftp_folder):
        """Initialise with 'settings.FTP_STATIC_DIR'."""
        self.ftp_folder = ftp_folder

    def _read_courses(self, university, department):
        folder = os.path.join(
            self.ftp_folder,
            'academy',
            university,
            department,
        )
        order = 0
        folders = os.listdir(folder)
        for course in folders:
            path = os.path.join(folder, course)
            if os.path.isdir(path):
                order = order + 1
                _update_course(university, department, order, course)
                self._read_topics(university, department, course)

    def _read_departments(self, university):
        folder = os.path.join(
            self.ftp_folder,
            'academy',
            university,
        )
        folders = os.listdir(folder)
        for department in folders:
            path = os.path.join(folder, department)
            if os.path.isdir(path):
                _update_department(university, department)
                self._read_courses(university, department)

    def _read_topics(self, university, department, course):
        folder = os.path.join(
            self.ftp_folder,
            'academy',
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
                _update_topic(
                    university,
                    department,
                    course,
                    number_from_string(topic),
                    os.path.join(
                        'academy',
                        university,
                        department,
                        course,
                        topic,
                    ),
                    topic
                )

    def _read_universities(self):
        folder = os.path.join(
            self.ftp_folder,
            'academy'
        )
        folders = os.listdir(folder)
        for university in folders:
            path = os.path.join(folder, university)
            if os.path.isdir(path):
                _update_university(university)
                self._read_departments(university)

    def update(self):
        """Update the database based on the folder structure."""
        self._read_universities()
