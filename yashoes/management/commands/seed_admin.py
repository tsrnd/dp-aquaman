from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'Seed data'

    def handle(self, *args, **options):
        self.stdout.write('Create account admin for every body')
        from yashoes.seeds import user
        user.create_superuser()
