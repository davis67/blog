from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.utils import timezone
from . import forms, models


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


class PostCreate(FormView):
    """Create view Definition """

    def get(self, request):

        form = forms.PostCreateForm()

        return render(request, "posts/post_create_form.html", {"form": form})

    def post(self, request):
        form = forms.PostCreateForm(request.POST)
        print(request.user)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect(reverse("core:home"))

        return render(request, "posts/post_create_form.html", {"form": form})
