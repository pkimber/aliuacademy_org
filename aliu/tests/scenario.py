"""Set-up the default scenario for demo and testing purposes."""

import os

from django.conf import settings

from aliu.service import FtpReader


def default_scenario_aliu():
    """Default scenario for the academy."""
    FtpReader(settings.FTP_STATIC_DIR).update()
