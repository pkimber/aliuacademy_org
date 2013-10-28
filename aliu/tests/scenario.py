from aliu.tests.model_maker import (
    make_course,
    make_department,
    make_university,
    make_topic,
)


def default_scenario_aliu():
    uni = make_university('exeter', 'Exeter')
    dept = make_department(uni, 'Mathematics')
    course = make_course(dept, 'Advanced')
    make_topic(course, 'Basic')
    make_topic(course, 'Experienced')
    course = make_course(dept, 'Beginner')
    make_department(uni, 'Engineering')
    uni = make_university('southampton', 'Southampton')
    make_department(uni, 'Electrical Engineering')
    make_department(uni, 'Electronics')
    make_department(uni, 'Computing')
