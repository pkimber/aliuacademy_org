# -*- encoding: utf-8 -*-
from django.core.management.base import BaseCommand
from login.tests.scenario import (
    default_scenario_login,
    user_contractor,
)


class Command(BaseCommand):

    help = "Create demo data for 'login'"

    def handle(self, *args, **options):
        default_scenario_login()
        user_contractor()
        print("Created 'login' demo data...")
