"""Service class."""

import os

from walkdir import filtered_walk

from .models import University
from aliu.tests.model_maker import make_university


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
        folders = os.listdir(folder)
        for course in folders:
            path = os.path.join(folder, course)
            if os.path.isdir(path):
                print '    {}'.format(course)
                self._read_topics(path, course)

    def _read_departments(self, folder, university):
        folders = os.listdir(folder)
        for department in folders:
            path = os.path.join(folder, department)
            if os.path.isdir(path):
                print '  {}'.format(department)
                self._read_courses(path, university, department)

    def _read_topics(self, folder, course):
        folders = os.listdir(folder)
        for topic in folders:
            path = os.path.join(folder, topic)
            if os.path.isfile(path):
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

    def read(self):
        self._read_universities()
        return



        """Parse the folder and files in the FTP folder."""
        first_pass = True
        walk = filtered_walk(self.ftp_folder)
        for path, subdirs, files in walk:
            print
            if first_pass:
                first_pass = False
                _universities(path, subdirs)
            else:
                _courses(path, subdirs, files)
