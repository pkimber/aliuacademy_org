from base.tests.model_maker import clean_and_save

from aliu.models import (
    University,
)


def make_university(slug, name, **kwargs):
    return clean_and_save(
        University(
            slug=slug,
            name=name,
            **kwargs
        )
    )
