from django.contrib.auth.models import AbstractUser
from core import models as core_models
from django.db import models


class User(AbstractUser, core_models.TimeStampedModel):
    """Custom user model """
    GENDER_MALE = "male"
    GENDER_FEMALE = "female"

    GENDER_CHOICES = (
        (GENDER_MALE, 'Male'),
        (GENDER_FEMALE, 'Female'),
    )
    gender = models.CharField(choices=GENDER_CHOICES,
                              max_length=10, blank=True)
    avatar = models.ImageField(blank=True, upload_to='avatar/')
    superhost = models.BooleanField(default=False)
