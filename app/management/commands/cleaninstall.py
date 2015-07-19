from django.core.management import call_command
from django.core.management.base import BaseCommand

__author__ = 'baran'


class Command(BaseCommand):
    def handle(self, *args, **options):
        call_command('droptables', **options)
        call_command('syncdb', interactive=False)
        call_command('rebuild_index', **options)






