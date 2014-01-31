"""Database models for Aliu's Academy."""

import os

from django.db import models

import reversion

from base.model_utils import (
    ftp_file_store,
    TimeStampedModel,
)


class University(TimeStampedModel):

    """University e.g. MIT."""

    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100, unique=True)

reversion.register(University)


class Department(TimeStampedModel):

    """Department at the University."""

    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    university = models.ForeignKey(University)

    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        unique_together = ('university', 'folder_name',)

reversion.register(Department)


class Course(TimeStampedModel):

    """Course e.g. Introduction to Computer Science."""

    order = models.IntegerField()
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)

    class Meta:
        ordering = ('order',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        unique_together = ('department', 'folder_name',)

reversion.register(Course)


class Topic(TimeStampedModel):

    """File stores the Video for the Topic."""

    order = models.IntegerField()
    name = models.CharField(max_length=150)
    video = models.FileField(
        max_length=300,
        upload_to='video/%Y/%m/%d',
        storage=ftp_file_store,
    )
    course = models.ForeignKey(Course)

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        unique_together = ('course', 'video',)

    def __unicode__(self):
        return unicode('{}'.format(self.name))

    def download_file_name(self):
        return os.path.basename(self.video.name)


reversion.register(Topic)
