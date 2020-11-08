from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from django.views.generic import DetailView
from django.views.generic.edit import UpdateView
from . import forms, mixins, models


class SignUpView(SuccessMessageMixin, mixins.LoggedOutOnlyView, View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(self.request, "users/signup.html", {"form": form})

    def post(self, request):
        form = forms.SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')

            user = authenticate(
                request=request, username=username, password=password)

            if user is not None:
                login(request, user)
                next_arg = request.GET.get("next")
                if next_arg is not None:
                    return next_arg
                return redirect(reverse('core:home'))
            return render(request, "users/signup.html", {"form": form})


class LoginView(mixins.LoggedOutOnlyView, View):
    def get(self, request):
        form = forms.LoginForm()
        return render(request, "users/login.html", {"form": form})

    def post(self, request):
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            password = form.cleaned_data.get("password")
            loggedInUser = models.User.objects.get(email=email)
            user = authenticate(
                request=request, username=loggedInUser.username, password=password
            )
            if user is not None:
                login(request, user)
                success_message = "Welcome Back!"
                next_arg = request.GET.get("next")
                if next_arg is not None:
                    return next_arg
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})


class AddProfileView(mixins.LoggedInOnlyView, View):

    def get(self, request):
        form = forms.AddProfilePictureForm()
        return render(request, "users/add-profile-picture.html", {"form": form})

    def post(self, request):
        form = forms.AddProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            avatar = form.cleaned_data.get("avatar")
            loggedInUser = models.User.objects.get(email=request.user.email)
            loggedInUser.avatar = avatar
            loggedInUser.save()
            success_message = "Avatar added!"
            return redirect(reverse("core:home"))

        return render(request, "posts/post_create_form.html", {"form": form})


class UserProfileView(DetailView):
    model = models.User
    context_object_name = "user_obj"


class UpdateProfileView(UpdateView):
    model = models.User
    template_name = "users/update-profile.html"
    fields = ("first_name", "last_name", "username",
              "email", "gender", "avatar",)

    def get_object(self, queryset=None):
        return self.request.user


def log_out(request):
    logout(request)
    return redirect(reverse("users:login"))
