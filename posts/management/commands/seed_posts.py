import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed

from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int,
                            help="How many posts do you want to seed?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_categories = post_models.Category.objects.all()

        seeder.add_entity(post_models.Post, number, {
            "author": lambda x: random.choice(all_users),
            "photo": lambda x: f"/posts_photos/{random.randint(1,7)}.jpg",
            "category": lambda x: random.choice(all_categories),
            "authorized_by": None
        })

        created_posts = seeder.execute()
        cleaned_posts = flatten(list(created_posts.values()))

        self.stdout.write(f"{len(cleaned_posts)} Posts created!")
