"""Database models for Aliu's Academy."""

from django.db import models

import reversion

from base.model_utils import (
    ftp_file_store,
    TimeStampedModel,
)


class University(TimeStampedModel):

    """University e.g. MIT."""

    slug = models.SlugField()
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)

reversion.register(University)


class Department(TimeStampedModel):

    """Department at the University."""

    name = models.CharField(max_length=100)
    university = models.ForeignKey(University)

reversion.register(Department)


class Course(TimeStampedModel):

    """Course e.g. Introduction to Computer Science."""

    order = models.IntegerField()
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)

reversion.register(Course)


class Topic(TimeStampedModel):

    """File stores the Video for the Topic."""

    order = models.IntegerField()
    name = models.CharField(max_length=100)
    video = models.FileField(
        upload_to='video/%Y/%m/%d', storage=ftp_file_store
    )
    course = models.ForeignKey(Course)

reversion.register(Topic)
