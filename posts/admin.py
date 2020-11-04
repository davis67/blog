from django.contrib import admin
from . import models


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at",)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "description",)
