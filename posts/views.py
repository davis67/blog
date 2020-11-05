from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from django.views import View
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
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect(reverse("core:home"))

        return render(request, "posts/post_create_form.html", {"form": form})


class AddReply(View):
    model = models.Reply

    def post(self, request, pk):
        form = forms.AddReplyForm(request.POST)
        comment = models.Comment.objects.get(pk=pk)
        if form.is_valid():
            description = form.cleaned_data.get("description")
            models.Reply.objects.create(
                description=description, comment=comment, author=request.user)
            # redirect back
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


class AddComment(View):
    model = models.Comment

    def post(self, request, pk):
        form = forms.AddCommentForm(request.POST)
        post = models.Post.objects.get(pk=pk)
        if form.is_valid():
            description = form.cleaned_data.get("description")
            models.Comment.objects.create(
                description=description, post=post, author=request.user)
            # redirect back
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
