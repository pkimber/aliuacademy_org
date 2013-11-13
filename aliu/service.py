"""Service class."""

import os

from .models import (
    Course,
    Department,
    Topic,
    University,
)

from aliu.tests.model_maker import (
    make_course,
    make_department,
    make_topic,
    make_university,
)


class AcademyError(Exception):

    """Exception class for the Aliu Academy app."""

    def __init__(self, value):
        Exception.__init__(self)
        self.value = value

    def __str__(self):
        return repr('%s, %s' % (self.__class__.__name__, self.value))


def _read_courses(folder, university, department):
    order = 0
    folders = os.listdir(folder)
    for course in folders:
        path = os.path.join(folder, course)
        if os.path.isdir(path):
            order = order + 1
            _update_course(university, department, order, course)
            _read_topics(path, university, department, course)


def _read_departments(folder, university):
    folders = os.listdir(folder)
    for department in folders:
        path = os.path.join(folder, department)
        if os.path.isdir(path):
            _update_department(university, department)
            _read_courses(path, university, department)


def _read_topics(folder, university, department, course):
    order = 0
    folders = os.listdir(folder)
    for topic in folders:
        path = os.path.join(folder, topic)
        if os.path.isfile(path):
            order = order + 1
            _update_topic(university, department, course, order, topic)


def _update_course(university, department, order, course):
    univ = University.objects.get(folder_name=university)
    dept = Department.objects.get(university=univ, folder_name=department)
    try:
        Course.objects.get(
            department=dept,
            folder_name=course
        )
    except Course.DoesNotExist:
        make_course(
            department=dept,
            order=order,
            folder_name=course,
        )


def _update_topic(university, department, course, order, topic):
    univ = University.objects.get(folder_name=university)
    dept = Department.objects.get(university=univ, folder_name=department)
    cour = Course.objects.get(department=dept, folder_name=course)
    try:
        Topic.objects.get(
            course=cour,
            video=topic,
        )
    except Topic.DoesNotExist:
        make_topic(
            course=cour,
            order=order,
            file_name=topic,
        )


def _update_department(university, department):
    uni = University.objects.get(folder_name=university)
    try:
        Department.objects.get(
            university=uni,
            folder_name=department
        )
    except Department.DoesNotExist:
        make_department(
            university=uni,
            folder_name=department,
        )


def _update_university(university):
    try:
        University.objects.get(folder_name=university)
    except University.DoesNotExist:
        make_university(
            slug=university.lower(),
            folder_name=university,
        )


class FtpReader(object):

    """
    Aliu will upload videos via FTP.

    Read the folder structure and update the database to reflect it.

    """

    def __init__(self, ftp_folder):
        """Initialise with 'settings.FTP_STATIC_DIR'."""
        self.academy_folder = os.path.join(ftp_folder, 'academy')

    def _read_universities(self):
        folders = os.listdir(self.academy_folder)
        for university in folders:
            path = os.path.join(self.academy_folder, university)
            if os.path.isdir(path):
                _update_university(university)
                _read_departments(path, university)

    def update(self):
        """Update the database based on the folder structure."""
        self._read_universities()
