from base.tests.model_maker import clean_and_save

from aliu.models import (
    Department,
    University,
)


def make_department(university, name, **kwargs):
    return clean_and_save(
        Department(
            university=university,
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
