# -*- encoding: utf-8 -*-

from __future__ import unicode_literals
from django.core.management.base import BaseCommand

from aliu.tests.scenario import default_scenario_aliu


class Command(BaseCommand):

    help = "Initialise 'aliuacademy_org' application"

    def handle(self, *args, **options):
        default_scenario_aliu()
        print("Initialised 'aliuacademy_org' app...")
