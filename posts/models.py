from django.db import models
from core import models as core_models


class Category(core_models.TimeStampedModel):
    """ Category Model Definition """

    name = models.CharField(max_length=140)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Comment(core_models.TimeStampedModel):
    """ Comment Model Definition"""

    description = models.TextField()
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)
    post = models.ForeignKey(
        "Post", related_name="comments", on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Reply(core_models.TimeStampedModel):
    """ Reply Model Definition"""

    description = models.TextField()
    comment = models.ForeignKey(
        "Comment", related_name="replies", on_delete=models.CASCADE, blank=True, null=True)
    author = models.ForeignKey("users.User", on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Post(core_models.TimeStampedModel):
    """ Post Model Definition """

    title = models.CharField(max_length=140)
    description = models.TextField()
    photo = models.ImageField(blank=True,)
    author = models.ForeignKey(
        "users.User", related_name="author", on_delete=models.CASCADE)
    is_published = models.BooleanField(default=False)
    authorized_by = models.ForeignKey(
        "users.User", on_delete=models.SET_NULL, null=True, blank=True, default=None)
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE)
