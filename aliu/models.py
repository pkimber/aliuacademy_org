from django.db import models

import reversion

from base.model_utils import TimeStampedModel


class University(TimeStampedModel):
    slug = models.SlugField()
    name = models.CharField(max_length=100)

reversion.register(University)


class Department(TimeStampedModel):
    name = models.CharField(max_length=100)
    university = models.ForeignKey(University)

reversion.register(Department)


class Course(TimeStampedModel):
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)

reversion.register(Course)


class Topic(TimeStampedModel):
    name = models.CharField(max_length=100)
    course = models.ForeignKey(Course)

reversion.register(Topic)
