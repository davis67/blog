from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.views import View
from . import forms, models


class SignUpView(View):
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
                return redirect(reverse('core:home'))
            return render(request, "users/signup.html", {"form": form})


class LoginView(View):
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
                return redirect(reverse("core:home"))

        return render(request, "users/login.html", {"form": form})


def log_out(request):
    logout(request)
    return redirect(reverse("users:login"))
