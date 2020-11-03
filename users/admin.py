from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomerUserAdmin(UserAdmin):
    """Custom User Admin """
    fieldsets = (
        ("Custom Profile", {
            "fields": (
                "avatar",
                "gender",
                "superhost",
            ),
        }),
    )
    list_filter = ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "gender",
        "is_active",
        "superhost",
    )
