from base.tests.model_maker import clean_and_save

from aliu.models import (
    Course,
    Department,
    Topic,
    University,
)


def make_course(department, name, **kwargs):
    return clean_and_save(
        Course(
            department=department,
            name=name,
            **kwargs
        )
    )


def make_department(university, name, **kwargs):
    return clean_and_save(
        Department(
            university=university,
            name=name,
            **kwargs
        )
    )


def make_topic(course, name, **kwargs):
    return clean_and_save(
        Topic(
            course=course,
            name=name,
            **kwargs
        )
    )


def make_university(slug, name, **kwargs):
    return clean_and_save(
        University(
            slug=slug,
            name=name,
            **kwargs
        )
    )
