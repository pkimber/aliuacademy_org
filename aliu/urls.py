from django.conf.urls import (
    patterns, url
)

from .views import (
    DepartmentListView,
    UniversityListView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^university/$',
        view=UniversityListView.as_view(),
        name='aliu.university.list'
        ),
    url(regex=r'^department/(?P<slug>[-\w\d]+)/$',
        view=DepartmentListView.as_view(),
        name='aliu.department.list'
        ),
)
