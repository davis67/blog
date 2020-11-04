from django.core.management.base import BaseCommand
from posts.models import Category


class Command(BaseCommand):
    def handle(self, *args, **options):
        categories = [
            "Technology",
            "Agriculture",
            "Environment",
            "Health & Nutrition",
            "Neighbourhood",
            "Sports",
            "Culture",
        ]
        for category in categories:
            Category.objects.create(name=category)
        self.stdout.write(self.style.SUCCESS(
            f"{len(categories)} Categories created!"))
