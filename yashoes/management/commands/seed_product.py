from django.core.management.base import BaseCommand

from yashoes.seeds import product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Create product data')
        product.create_product()
