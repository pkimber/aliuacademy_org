# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.conf.urls import (
    patterns, url
)

from .views import (
    AboutView,
    CourseTopicListView,
    DepartmentCourseListView,
    TopicDetailView,
    UniversityDepartmentListView,
    UniversityListView,
    UniversitiesView,
    VisionView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^about/$',
        view=AboutView.as_view(),
        name='aliu.about'
        ),
    url(regex=r'^academy/department/(?P<pk>\d+)/$',
        view=DepartmentCourseListView.as_view(),
        name='aliu.department.course.list'
        ),
    url(regex=r'^academy/university/(?P<slug>[-\w\d]+)/$',
        view=UniversityDepartmentListView.as_view(),
        name='aliu.university.department.list'
        ),
    url(regex=r'^academy/course/(?P<pk>\d+)/$',
        view=CourseTopicListView.as_view(),
        name='aliu.course.topic.list'
        ),
    url(regex=r'^academy/university/$',
        view=UniversityListView.as_view(),
        name='aliu.university.list'
        ),
    url(regex=r'^academy/topic/(?P<pk>\d+)/$',
        view=TopicDetailView.as_view(),
        name='aliu.topic.detail'
        ),
    url(regex=r'^universities/$',
        view=UniversitiesView.as_view(),
        name='aliu.universities'
        ),
    url(regex=r'^vision/$',
        view=VisionView.as_view(),
        name='aliu.vision'
        ),
)
