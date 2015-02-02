# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand

from web.service import VideoReader


class Command(BaseCommand):

    help = "Initialise 'aliuacademy_org' application"

    def handle(self, *args, **options):
        VideoReader(settings.MEDIA_ROOT).update()
        print("Initialised '{}' app...".format(settings.SITE_NAME))
