from django.conf.urls import (
    patterns, url
)

from .views import (
    UniversityListView,
)


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=UniversityListView.as_view(),
        name='aliu.university.list'
        ),
)
