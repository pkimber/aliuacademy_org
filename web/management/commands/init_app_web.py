# -*- encoding: utf-8 -*-
from __future__ import unicode_literals

from django.conf import settings
from django.core.management.base import BaseCommand

from web.tests.scenario import default_scenario_web


class Command(BaseCommand):

    help = "Initialise 'aliuacademy_org' application"

    def handle(self, *args, **options):
        default_scenario_web()
        print("Initialised '{}' app...".format(settings.SITE_NAME))
