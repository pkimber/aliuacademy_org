from django.conf.urls import (
    patterns, url
)

from .views import (
    CourseListView,
    DepartmentListView,
    TopicListView,
    UniversityListView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^course/(?P<pk>\d+)/$',
        view=CourseListView.as_view(),
        name='aliu.course.list'
        ),
    url(regex=r'^department/(?P<slug>[-\w\d]+)/$',
        view=DepartmentListView.as_view(),
        name='aliu.department.list'
        ),
    url(regex=r'^topic/(?P<pk>\d+)/$',
        view=TopicListView.as_view(),
        name='aliu.topic.list'
        ),
    url(regex=r'^university/$',
        view=UniversityListView.as_view(),
        name='aliu.university.list'
        ),
)
