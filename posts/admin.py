from django.contrib import admin
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
