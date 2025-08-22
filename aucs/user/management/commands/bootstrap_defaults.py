from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "Bootstrap default data from fixtures"

    def handle(self, *args, **kwargs):
        try:
            call_command("loaddata", "defaults.json")
            self.stdout.write(self.style.SUCCESS("Default data loaded from fixtures"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Default data already exists, skipping"))
from django.core.management.base import BaseCommand
from django.core.management import call_command
from django.db.utils import IntegrityError

class Command(BaseCommand):
    help = "Bootstrap default data from fixtures"

    def handle(self, *args, **kwargs):
        try:
            call_command("loaddata", "defaults.json")
            self.stdout.write(self.style.SUCCESS("Default data loaded from fixtures"))
        except IntegrityError:
            self.stdout.write(self.style.WARNING("Default data already exists, skipping"))
