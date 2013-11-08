"""Service class."""

from walkdir import filtered_walk


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
        self.ftp_folder = ftp_folder

    def read(self):
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
