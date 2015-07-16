from django.core.management.base import BaseCommand
from django.db import transaction, connection

__author__ = 'baran'


class Command(BaseCommand):
    def handle(self, *args, **options):
        c = connection.cursor()
        try:
            c.execute(
                "SELECT table_schema,table_name FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,table_name")
            rows = c.fetchall()
            for row in rows:
                print "dropping table: ", row[1]
                c.execute("DROP TABLE " + row[1] + " CASCADE")
        except:
            raise Exception('Unable to drop database tables.')

