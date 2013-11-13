from django.conf.urls import (
    patterns, url
)

from .views import (
    CourseTopicListView,
    DepartmentCourseListView,
    TopicDetailView,
    UniversityDepartmentListView,
    UniversityListView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^department/(?P<pk>\d+)/$',
        view=DepartmentCourseListView.as_view(),
        name='aliu.department.course.list'
        ),
    url(regex=r'^university/(?P<slug>[-\w\d]+)/$',
        view=UniversityDepartmentListView.as_view(),
        name='aliu.university.department.list'
        ),
    url(regex=r'^course/(?P<pk>\d+)/$',
        view=CourseTopicListView.as_view(),
        name='aliu.course.topic.list'
        ),
    url(regex=r'^universities/$',
        view=UniversityListView.as_view(),
        name='aliu.university.list'
        ),
    url(regex=r'^topic/(?P<pk>\d+)/$',
        view=TopicDetailView.as_view(),
        name='aliu.topic.detail'
        ),
)
