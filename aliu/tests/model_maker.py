from base.tests.model_maker import clean_and_save

from aliu.models import (
    Course,
    Department,
    Topic,
    University,
)


def make_course(department, order, name, **kwargs):
    return clean_and_save(
        Course(
            department=department,
            order=order,
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


def make_topic(course, order, name, **kwargs):
    return clean_and_save(
        Topic(
            course=course,
            order=order,
            name=name,
            **kwargs
        )
    )


def make_university(slug, folder_name, **kwargs):
    defaults = {
        'name': folder_name,
    }
    defaults.update(kwargs)
    return clean_and_save(
        University(
            slug=slug,
            name=defaults['name'],
            folder_name=folder_name,
            **kwargs
        )
    )
