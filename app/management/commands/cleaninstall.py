from django.core.management import call_command
from django.core.management.base import BaseCommand

from app.management.commands.droptables import Command as dtcommand


__author__ = 'baran'


class Command(BaseCommand):
    def handle(self, *args, **options):
        dtcommand().handle(args, options)
        call_command('syncdb', interactive=False)






