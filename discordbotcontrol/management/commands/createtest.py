from django.core.management.base import BaseCommand
from discordbotcontrol.models import TestModel
from discordbotcontrol.serializers import TestSerializer


class Command(BaseCommand):
    def add_arguments(self, parser):
        # Positional arguments
        parser.add_argument('name')

        # Named (optional) arguments
        parser.add_argument(
            '--desc',
            help='The data',
        )
        parser.add_argument(
            '--father',
            help='The data',
        )

    def handle(self, name, data="", **other):
        serializer = TestSerializer()
        test = serializer.create({'name': name, 'data': data})
        self.stdout.write(self.style.SUCCESS(
            'Successfully created TestModel with name {} and data: {}'.format(test.name, test.data)))
