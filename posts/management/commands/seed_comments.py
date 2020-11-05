import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed

from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int,
                            help="How many Comments do you want to seed?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_posts = post_models.Post.objects.all()

        seeder.add_entity(post_models.Comment, number, {
            "author": lambda x: random.choice(all_users),
            "post": lambda x: random.choice(all_posts),
        })

        created_comments = seeder.execute()
        cleaned_comments = flatten(list(created_comments.values()))

        self.stdout.write(f"{len(cleaned_comments)} Comments created!")
