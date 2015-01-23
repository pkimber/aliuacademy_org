# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""Database models for Aliu's Academy."""

import os

from django.db import models
from django.utils.text import slugify

import reversion

from base.model_utils import (
    ftp_file_store,
    TimeStampedModel,
)


class UniversityManager(models.Manager):

    def create_university(self, folder_name):
        university = self.model(
            slug=slugify(folder_name),
            name=folder_name,
            folder_name=folder_name,
        )
        university.save()
        return university


class University(TimeStampedModel):

    """University e.g. MIT."""

    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100, unique=True)
    objects = UniversityManager()

    class Meta:
        ordering = ('slug',)

reversion.register(University)


class DepartmentManager(models.Manager):

    def create_department(self, university, folder_name):
        department = self.model(
            university=university,
            name=folder_name,
            folder_name=folder_name,
        )
        department.save()
        return department


class Department(TimeStampedModel):

    """Department at the University."""

    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    university = models.ForeignKey(University)
    objects = DepartmentManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        unique_together = ('university', 'folder_name',)

reversion.register(Department)


class CourseManager(models.Manager):

    def create_course(self, department, order, folder_name):
        course = self.model(
            department=department,
            order=order,
            name=folder_name,
            folder_name=folder_name,
        )
        course.save()
        return course


class Course(TimeStampedModel):

    """Course e.g. Introduction to Computer Science."""

    order = models.IntegerField()
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)
    objects = CourseManager()

    class Meta:
        ordering = ('order',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        unique_together = ('department', 'folder_name',)

reversion.register(Course)


class TopicManager(models.Manager):

    def create_topic(self, course, order, file_path):
        name = os.path.basename(file_path)
        name, _ = os.path.splitext(name)
        topic = self.model(
            order=order,
            name=name,
            video=file_path,
            course=course,
        )
        topic.save()
        return topic


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
    objects = TopicManager()

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        unique_together = ('course', 'video',)

    def __str__(self):
        return '{}'.format(self.name)

    def download_file_name(self):
        return os.path.basename(self.video.name)

reversion.register(Topic)
