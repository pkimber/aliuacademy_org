# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

"""Set-up the default scenario for demo and testing purposes."""

import os

from django.conf import settings

from web.service import FtpReader


def default_scenario_web():
    """Default scenario for the academy."""
    FtpReader(settings.FTP_STATIC_DIR).update()
