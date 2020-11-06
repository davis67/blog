from django.contrib import admin
from django.utils.html import mark_safe
from . import models


class ReplyInline(admin.TabularInline):
    model = models.Reply


class CommentInline(admin.StackedInline):
    model = models.Comment
    inlines = (ReplyInline,)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at",)


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):

    inlines = [CommentInline, ]

    list_display = ("title", "description",)

    # def get_thumbnail(self, obj):
    #     return mark_safe(f'<img width="70px" src="{obj.photo.url}" />')

    # get_thumbnail.short_description = "Photo"
