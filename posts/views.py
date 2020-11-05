from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.utils import timezone
from . import models


class HomeView(ListView):
    """HomeView Definition """
    model = models.Post

    paginate_by = 10
    ordering = "created_at"
    paginate_orphans = 5

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        now = timezone.now()
        context["now"] = now
        return context


class PostDetail(DetailView):
    """Detail view Definition """
    model = models.Post
