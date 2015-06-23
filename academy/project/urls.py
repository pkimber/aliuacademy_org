# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    include,
    patterns,
    url,
)
from django.conf.urls.static import static
from django.contrib import admin

from login.views import RegisterCreateView
from web.views import AboutView
from web.views import SettingsView
from web.views import DBRebuildView


admin.autodiscover()


urlpatterns = patterns(
    '',
    url(regex=r'^$',
        view=AboutView.as_view(),
        name='project.home'
        ),
    url(regex=r'^',
        view=include('login.urls')
        ),
    url(regex=r'^rebuilddb/',
        view=DBRebuildView.as_view(),
        name='project.settings'
        ),
    url(regex=r'^admin/',
        view=include(admin.site.urls)
        ),
    url(regex=r'^settings/$',
        view=SettingsView.as_view(),
        name='project.settings'
        ),
    url(regex=r'^web/',
        view=include('web.urls')
        ),
    url(regex=r'^accounts/register/$',
        view=RegisterCreateView.as_view(),
        name='register'
        ),
)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
#   ^ helper function to return a URL pattern for serving files in debug mode.
# https://docs.djangoproject.com/en/1.5/howto/static-files/#serving-files-uploaded-by-a-user
