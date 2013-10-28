from aliu.tests.model_maker import (
    make_department,
    make_university,
)


def default_scenario_aliu():
    uni = make_university('exeter', 'Exeter')
    make_department(uni, 'Mathematics')
    make_department(uni, 'Engineering')
    uni = make_university('southampton', 'Southampton')
    make_department(uni, 'Electrical Engineering')
    make_department(uni, 'Electronics')
    make_department(uni, 'Computing')
