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
    VisionView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^about/$',
        view=AboutView.as_view(),
        name='aliu.about'
        ),
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
    url(regex=r'^vision/$',
        view=VisionView.as_view(),
        name='aliu.vision'
        ),
)
