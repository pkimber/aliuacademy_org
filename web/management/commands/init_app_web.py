# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand

from web.service import FtpReader


class Command(BaseCommand):

    help = "Initialise 'aliuacademy_org' application"

    def handle(self, *args, **options):
        FtpReader(settings.FTP_STATIC_DIR).update()
        print("Initialised '{}' app...".format(settings.SITE_NAME))
