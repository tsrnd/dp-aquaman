from django.core.management.base import BaseCommand

from yashoes.seeds import brand


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create category data')
        brand.create_brand()
