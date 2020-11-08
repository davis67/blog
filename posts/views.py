from django.shortcuts import render, redirect, reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormView
from django.http import HttpResponseRedirect

from django.views import View
from django.urls import reverse_lazy
from django.utils import timezone
from . import forms, models
from users import mixins


class HomeView(mixins.MustAddProfilePictureAfterSignUp, mixins.LoggedOutOnlyView, ListView):
    """HomeView Definition """
    model = models.Post

    def get(self, request, *args, **kwargs):
        self.paginate_by = 10
        self.ordering = "-created_at"
        self.paginate_orphans = 5
        self.object_list = self.get_queryset()
        context = super().get_context_data(*args, **kwargs)
        context['categories'] = models.Category.objects.all()
        context["now"] = timezone.now()
        return render(request, "posts/post_list.html", context)

    def get_queryset(self):
        passed_category = self.kwargs.get('category')
        if passed_category is not None:
            category = models.Category.objects.get(name=passed_category)
            return models.Post.objects.filter(category=category.id)
        return models.Post.objects.all()


class PostDetail(DetailView):
    """Detail view Definition """
    model = models.Post


class PostCreate(mixins.LoggedInOnlyView, FormView):
    """Create view Definition """

    def get(self, request):

        form = forms.PostCreateForm()

        return render(request, "posts/post_create_form.html", {"form": form})

    def post(self, request):
        form = forms.PostCreateForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            form.save()
            return redirect(reverse("core:home"))

        return render(request, "posts/post_create_form.html", {"form": form})


class PostUpdate(mixins.LoggedInOnlyView, View):
    def get(self, request, pk):
        post = models.Post.objects.get(pk=pk)
        if post.author == request.user:
            form = forms.PostCreateForm(instance=post)
            return render(request, "posts/post_update_form.html", {"form": form, "post": post})
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

    def post(self, request, pk):
        post = models.Post.objects.get(pk=pk)
        if post.author == request.user:
            form = forms.PostCreateForm(
                request.POST, request.FILES, instance=post)
            if form.is_valid():
                form.save()
                # redirect back
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
        return HttpResponseRedirect('/')


class PostDelete(mixins.LoggedInOnlyView, View):
    def get(self, request, pk):
        post = models.Post.objects.get(pk=pk)
        if post.author == request.user:
            return render(request, "posts/confirm_post_delete.html", {"post": post})
        return redirect(reverse("core:home"))

    def post(self, request, pk):
        post = models.Post.objects.get(pk=pk)
        if post.author == request.user:
            post.delete()
            return redirect(reverse("core:home"))
        return redirect(reverse("core:home"))


class AddReply(mixins.LoggedInOnlyView, View):
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
