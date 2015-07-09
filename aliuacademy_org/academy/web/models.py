# -*- encoding: utf-8 -*-
"""Database models for Aliu's Academy."""

import os

from django.conf import settings
from django.db import models
from django.db.models import Sum
from django.utils.text import slugify

import reversion

from base.model_utils import (
    ftp_file_store,
    TimeStampedModel,
)

class FlaggedTimeStampedModel(TimeStampedModel):
    """
    An abstract base class model that provides additional shared flags for Videos DB
    """
    is_active = models.IntegerField(default=1)

    class Meta:
        abstract = True

        
class FlaggedTimeStampedManager(models.Manager):
    """
    An abstract base class model that provides additional shared flags for Videos DB
    """
    def deactivate_all(self):
        self.model.objects.all().update(is_active=0)

    class Meta:
        abstract = True

        
class ActiveFlagTimeStampedManager(models.Manager):
    """
    A class to only return active Unis, Departs, Courses or Topics
    """
    def get_queryset(self):
        return super(ActiveFlagTimeStampedManager, self).get_queryset().filter(is_active=1)    
          
   

        
class UniversityManager(FlaggedTimeStampedManager):

    def create_university(self, folder_name):
        university = self.model(
            slug=slugify(folder_name),
            name=folder_name,
            folder_name=folder_name,
        )        
        university.save()
        return university

    def update_university(self, university):
        try:
            uni_match = self.model.objects.get(folder_name=university)
            uni_match.is_active = 1  
            uni_match.save()
        except University.DoesNotExist:
            self.create_university(folder_name=university)

           
    
class University(FlaggedTimeStampedModel):

    """University e.g. MIT."""

    slug = models.SlugField(max_length=100)
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100, unique=True)
    objects = UniversityManager()
    active_objects = ActiveFlagTimeStampedManager()

    class Meta:
        ordering = ('slug',)

reversion.register(University)


class DepartmentManager(FlaggedTimeStampedManager):
        
    def create_department(self, university, folder_name):
        department = self.model(
            university=university,
            name=folder_name,
            folder_name=folder_name,
        )
        department.save()
        return department

    def update_department(self, university, department):
        uni = University.objects.get(folder_name=university)
        try:
            dept_match = self.model.objects.get(
                university=uni,
                folder_name=department
            )
            dept_match.is_active = 1
            dept_match.save()
        except Department.DoesNotExist:
            self.create_department(
                university=uni,
                folder_name=department,
            )


        
class Department(FlaggedTimeStampedModel):

    """Department at the University."""

    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    university = models.ForeignKey(University)
    objects = DepartmentManager()
    active_objects = ActiveFlagTimeStampedManager()

    class Meta:
        ordering = ('name',)
        verbose_name = 'Department'
        verbose_name_plural = 'Departments'
        unique_together = ('university', 'folder_name',)

reversion.register(Department)


class CourseManager(FlaggedTimeStampedManager):

    def create_course(self, department, order, folder_name):
        course = self.model(
            department=department,
            order=order,
            name=folder_name,
            folder_name=folder_name,
        )
        course.save()
        return course

    def update_course(self, university, department, order, course):
        univ = University.objects.get(folder_name=university)
        dept = Department.objects.get(university=univ, folder_name=department)
        try:
            crs_match = self.model.objects.get(
                department=dept,
                folder_name=course
            )
            crs_match.is_active = 1
            crs_match.save()
        except Course.DoesNotExist:
            self.create_course(
                department=dept,
                order=order,
                folder_name=course,
            )



class Course(FlaggedTimeStampedModel):

    """Course e.g. Introduction to Computer Science."""

    order = models.IntegerField()
    name = models.CharField(max_length=100)
    folder_name = models.CharField(max_length=100)
    department = models.ForeignKey(Department)
    objects = CourseManager()
    active_objects = ActiveFlagTimeStampedManager()

    class Meta:
        ordering = ('order',)
        verbose_name = 'Course'
        verbose_name_plural = 'Courses'
        unique_together = ('department', 'folder_name',)

reversion.register(Course)


class ActiveVideoManager(ActiveFlagTimeStampedManager):
    """
    A class to only return active Unis, Departs, Courses or Topics
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=1,
            file_type=Topic.VIDEO
        )


class ActiveWareManager(ActiveFlagTimeStampedManager):
    """
    A class to only return active Unis, Departs, Courses or Topics
    """
    def get_queryset(self):
        return super().get_queryset().filter(
            is_active=1,
            file_type=Topic.WARE
        )


class TopicManager(FlaggedTimeStampedManager):

    def create_topic(self, course, order, file_path, file_type):
        name = os.path.basename(file_path)
        name, _ = os.path.splitext(name)
        topic = self.model(
            order=order,
            name=name,
            video=file_path,
            course=course,
        )
        topic.file_type=file_type
        topic.save()
        return topic

    def update_topic(self, university, department, course, order, path, topic, file_type):
        univ = University.objects.get(folder_name=university)
        dept = Department.objects.get(university=univ, folder_name=department)
        cour = Course.objects.get(department=dept, folder_name=course)
        try:
            tpc_match = self.model.objects.get(
                course=cour,
                video=path,
            )
            tpc_match.is_active = 1
            tpc_match.save()
            return tpc_match
        except Topic.DoesNotExist:
            return self.create_topic(
                course=cour,
                order=order,
                file_path=path,
                file_type=file_type,
            )


class Topic(FlaggedTimeStampedModel):

    """File stores the Video for the Topic."""
    VIDEO = 1
    WARE = 2
    TOPIC_FILE_TYPES = (
        (VIDEO, 'Video'),
        (WARE, 'Ware'),
    )
    order = models.IntegerField()
    name = models.CharField(max_length=150)
    video = models.FileField(
        max_length=300,
        upload_to='video/%Y/%m/%d',
        storage=ftp_file_store,
    )
    course = models.ForeignKey(Course)
    file_type = models.IntegerField(choices=TOPIC_FILE_TYPES,default=VIDEO)
    objects = TopicManager()
    active_objects = ActiveVideoManager()
    active_ware = ActiveWareManager()

    class Meta:
        ordering = ('order', 'name')
        verbose_name = 'Topic'
        verbose_name_plural = 'Topics'
        unique_together = ('course', 'video',)

    def __str__(self):
        return '{}'.format(self.name)

    def download_file_name(self):
        return os.path.basename(self.video.name)

    @property
    def get_next(self):
        topic = Topic.active_objects.filter(
            course=self.course,
            order__gt=self.order,
        ).order_by(
            'order'
        )
        if topic:
            return topic[0]
        return None

    @property
    def get_prev(self):
        topic = Topic.active_objects.filter(
            course=self.course,
            order__lt=self.order,
        ).order_by(
            '-order'
        )
        if topic:
            return topic[0]
        return None

reversion.register(Topic)


class VideoViewManager(FlaggedTimeStampedManager):


    def get_topic_viewcounts(self, topic):    
        return self.model.objects.filter(viewed_topic=topic).aggregate(views=Sum('viewed'),dls=Sum('downloaded'))
    
    def create_view(self, topic, user, vw, dl):
        vd_view = self.model(
            viewed_topic=topic,
            viewer=user,
            viewed=vw,
            downloaded=dl,
        )
        vd_view.save()
        return vd_view

    def add_view(self, topic, user, vw, dl):

        try:
            vd_view = self.model.objects.get(
                viewed_topic=topic,
                viewer=user,
            )
            vd_view.viewed += int(vw)
            vd_view.downloaded += int(dl)
            vd_view.save()
            return vd_view
            
        except VideoView.DoesNotExist:
           return self.create_view(
                topic=topic,
                user=user,
                vw=vw,
                dl=dl,
            )


    
class VideoView(TimeStampedModel):
    viewed = models.IntegerField(default=0)
    downloaded = models.IntegerField(default=0)
    viewer = models.ForeignKey(settings.AUTH_USER_MODEL)
    viewed_topic = models.ForeignKey(Topic)
    objects = VideoViewManager()


class TopicCommentManager(FlaggedTimeStampedManager):

    def add_comment(self, topic, user, cmt):
        new_tc = self.model(
            comment=cmt,
            commentator=user,
            comment_topic=topic
        )
        new_tc.save()
        return new_tc
    
class TopicComment(TimeStampedModel):
    comment = models.TextField(max_length=500)
    commentator = models.ForeignKey(settings.AUTH_USER_MODEL)
    comment_topic = models.ForeignKey(Topic)
    objects = TopicCommentManager()
    active_objects = ActiveFlagTimeStampedManager()

