from django.core.management.base import BaseCommand


class Command(BaseCommand):

    help = "Initialise 'aliuacademy_org' application"

    def handle(self, *args, **options):
        print "Initialised 'aliuacademy_org' app..."
