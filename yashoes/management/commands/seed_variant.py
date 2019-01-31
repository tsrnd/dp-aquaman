from django.core.management.base import BaseCommand

from yashoes.seeds import varant


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create variant data')
        varant.create_variant()
