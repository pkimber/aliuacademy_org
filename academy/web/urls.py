# -*- encoding: utf-8 -*-
from django.conf.urls import (
    patterns,
    url,
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
    VideoViewListView,    
    AjaxCommandView,
    DownloadMediaView
)


urlpatterns = patterns(
    '',
    url(regex=r'^about/$',
        view=AboutView.as_view(),
        name='web.about'
        ),
    url(regex=r'^academy/department/(?P<pk>\d+)/$',
        view=DepartmentCourseListView.as_view(),
        name='web.department.course.list'
        ),
    url(regex=r'^academy/university/(?P<slug>[-\w\d]+)/$',
        view=UniversityDepartmentListView.as_view(),
        name='web.university.department.list'
        ),
    url(regex=r'^academy/course/(?P<pk>\d+)/$',
        view=CourseTopicListView.as_view(),
        name='web.course.topic.list'
        ),
    url(regex=r'^academy/university/$',
        view=UniversityListView.as_view(),
        name='web.university.list'
        ),
    url(regex=r'^academy/topic/(?P<pk>\d+)/$',
        view=TopicDetailView.as_view(),
        name='web.topic.detail'
        ),
    url(regex=r'^universities/$',
        view=UniversitiesView.as_view(),
        name='web.universities'
        ),
    url(regex=r'^userprofile/$',
        view=VideoViewListView.as_view(),
        name='web.userprofile'
        ),
    url(regex=r'^vision/$',
        view=VisionView.as_view(),
        name='web.vision'
        ),
    url(regex=r'^ajaxcall/(?P<cmd>.*)/(?P<pk>\d+)/$',
        view=AjaxCommandView,
        name='ajaxcall.command.topic'
        ),
    url(regex=r'^download/(?P<tpc_id>.*)/$',
        view=DownloadMediaView,
        name='download.media'
        ),
)
