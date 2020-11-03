from django.db import models


class Post(models.Model):
    """ Post Model Definition """

    title = models.CharField(max_length=140)
    description = models.TextField()
