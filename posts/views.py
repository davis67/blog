from django.shortcuts import render
from django.views.generic import ListView
from django.utils import timezone
from . import models


class HomeView(ListView):
    """HomeView Definition """
    model = models.Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context
