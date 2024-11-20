import csv

from django.core.management.base import BaseCommand
from phones.models import Phone

from datetime import datetime
from django.utils.text import slugify
class Command(BaseCommand):
    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        with open('phones.csv', 'r', encoding='utf-8') as file:
            phones = list(csv.DictReader(file, delimiter=';'))

        for item in phones:
            try:
                phone = Phone.objects.create(
                    id=int(item['id']),
                    name=item['name'],
                    price=int(item['price']),
                    image=item['image'],
                    release_date=datetime.strptime(item['release_date'], '%Y-%m-%d'),
                    lte_exists=item['lte_exists'].lower() == 'true',
                    slug=slugify(item['name'])
                )
                self.stdout.write(self.style.SUCCESS(f'Successfully added phone: {phone.name}'))
            except Exception as e:

                self.stdout.write(self.style.ERROR(f'Error adding phone: {e}'))