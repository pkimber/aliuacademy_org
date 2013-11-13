"""Service class."""

import os

from walkdir import filtered_walk

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


def _courses(path, subdirs, files):
    if subdirs:
        for course in subdirs:
            print 'course: {}'.format(course)
    elif files:
        for topic in files:
            print 'topic: {}'.format(topic)
    else:
        raise AcademyError('Cannot parse FTP folder structure')


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


def _universities(path, subdirs):
    for university in subdirs:
        print 'university: {}'.format(university)


class FtpReader(object):

    """
    Aliu will upload videos via FTP.

    Read the folder structure and update the database to reflect it.

    """

    def __init__(self, ftp_folder):
        """Initialise with 'settings.FTP_STATIC_DIR'."""
        self.academy_folder = os.path.join(ftp_folder, 'academy')

    def _read_courses(self, folder, university, department):
        order = 0
        folders = os.listdir(folder)
        for course in folders:
            path = os.path.join(folder, course)
            if os.path.isdir(path):
                order = order + 1
                print '    {}'.format(course)
                _update_course(university, department, order, course)
                self._read_topics(path, university, department, course)

    def _read_departments(self, folder, university):
        folders = os.listdir(folder)
        for department in folders:
            path = os.path.join(folder, department)
            if os.path.isdir(path):
                print '  {}'.format(department)
                _update_department(university, department)
                self._read_courses(path, university, department)

    def _read_topics(self, folder, university, department, course):
        order = 0
        folders = os.listdir(folder)
        for topic in folders:
            path = os.path.join(folder, topic)
            if os.path.isfile(path):
                order = order + 1
                _update_topic(university, department, course, order, topic)
                print '      {}'.format(topic)

    def _read_universities(self):
        print
        folders = os.listdir(self.academy_folder)
        for university in folders:
            path = os.path.join(self.academy_folder, university)
            if os.path.isdir(path):
                print university
                _update_university(university)
                self._read_departments(path, university)

    def update(self):
        self._read_universities()
