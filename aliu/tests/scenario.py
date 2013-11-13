import os

from aliu.service import FtpReader
#from aliu.tests.model_maker import (
#    make_course,
#    make_department,
#    make_university,
#    make_topic,
#)


def default_scenario_aliu():
    folder = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        'data',
        'ftp_static_dir',
    )
    FtpReader(folder).update()
    ## MIT
    #uni = make_university('mit', "MIT")
    #dept = make_department(
    #    uni,
    #    "Electrical Engineering and Computer Science (EECS)"
    #)
    #course = make_course(
    #    dept,
    #    1,
    #    "Introduction to computer science and programming"
    #)
    #make_topic(course, 1, "Introduction to the course")
    #make_topic(course, 2, "Core elements of a computer program")
    #course = make_course(dept, 2, "Circuits and Electronics")
    #make_topic(course, 1, "Introduction to the course")
    #make_topic(course, 2, "Core elements of a computer program")
    #dept = make_department(uni, "Mathematics")
    #course = make_course(dept, 1, "Linear algebra")
    #make_topic(course, 1, "The Geometry of linear equations")
    #make_topic(course, 2, "Matrices")
    #course = make_course(dept, 2, "Differential equations")
    ## edX
    #uni = make_university('edx', 'edX')
    #dept = make_department(uni, "Electrical engineering and Computer science")
    #course = make_course(dept, 1, "Software as a service")
    #course = make_course(dept, 2, "Foundation of computer graphics")
    #dept = make_department(uni, "Civil Engineering")
    #course = make_course(dept, 1, "Elements of structures")
