# -*- encoding: utf-8 -*-
from django.conf import settings
from django.conf.urls import (
    patterns,
    url,
)
from django.contrib.auth.views import (
    password_reset,
    password_reset_complete,
    password_reset_confirm,
    password_reset_done,
)
from django.core.urlresolvers import reverse_lazy

from .forms import PasswordResetNotifyForm
from .views import PasswordResetAuditListView


urlpatterns = patterns(
    '',
    url(regex=r'^accounts/login/$',
        view='django.contrib.auth.views.login',
        kwargs={
            'extra_context': {
                'testing': settings.TESTING, 'path': '/accounts/login/'
            },
            'template_name': 'project/login.html',
        },
        name='login'
        ),
    url(regex=r'^accounts/logout/$',
        view='django.contrib.auth.views.logout',
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'next_page': reverse_lazy('project.home'),
            'template_name': 'login/logged_out.html',
        },
        name='logout'
        ),
    url(regex=r'^accounts/password/change/$',
        view='django.contrib.auth.views.password_change',
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'template_name': 'project/password_change.html',
        },
        name='password_change'
        ),
    url(regex=r'^accounts/password/change/done/$',
        view='django.contrib.auth.views.password_change_done',
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'template_name': 'project/password_change_done.html',
        },
        name='password_change_done'
        ),
    url(regex=r'^accounts/password/reset/$',
        view=password_reset,
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'password_reset_form': PasswordResetNotifyForm,
            'template_name': 'project/password_reset.html'
        },
        name='password_reset'
        ),
    # https://westcountrycoders.co.uk/accounts/password/reset/NTMxNg/3sc-d2a52e19e0d239ea538e/
    # Reverse for 'password_reset_complete' with arguments '()' and keyword arguments '{}' not found. 0 pattern(s) tried: []
    # password_reset_complete
    url(regex=r'^accounts/password/reset/complete/$',
        view=password_reset_complete,
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'template_name': 'project/password_reset_complete.html'
        },
        name='password_reset_complete'
        ),
    url(regex=r'^accounts/password/reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        view=password_reset_confirm,
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'template_name': 'project/password_reset_confirm.html',
        },
        name='password_reset_confirm'
        ),
    url(regex=r'^accounts/password/reset/done/$',
        view=password_reset_done,
        kwargs={
            'extra_context': {'testing': settings.TESTING},
            'template_name': 'project/password_reset_done.html'
        },
        name='password_reset_done'
        ),
    url(regex=r'^accounts/password/reset/audit/report/$',
        view=PasswordResetAuditListView.as_view(),
        name='password_reset_audit_report'
        ),
)
