import random
from django.core.management.base import BaseCommand
from django.contrib.admin.utils import flatten
from django_seed import Seed

from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--number", default=2, type=int,
                            help="How many Replies do you want to seed?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        all_comments = post_models.Comment.objects.all()

        seeder.add_entity(post_models.Reply, number, {
            "author": lambda x: random.choice(all_users),
            "comment": lambda x: random.choice(all_comments),
        })

        created_replies = seeder.execute()
        cleaned_replies = flatten(list(created_replies.values()))

        self.stdout.write(f"{len(cleaned_replies)} Replies created!")
