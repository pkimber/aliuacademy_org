# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
from django.utils import timezone

from .factories import TEST_PASSWORD


def make_user(user_name, **kwargs):
    """ Some code copied from 'contrib.auth.models.create_user' """
    defaults = {
        'date_joined': timezone.now(),
        'is_active': True,
        'is_staff': False,
        'is_superuser': False,
    }
    defaults.update(kwargs)
    user = User(
        username=user_name,
        **defaults
    )
    user.set_password(TEST_PASSWORD)
    user.save()
    return user


def make_superuser(user_name):
    return User.objects.create_superuser(user_name, '', TEST_PASSWORD)
