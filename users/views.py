from django.shortcuts import render, reverse, redirect
from django.contrib.auth import authenticate, login
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

            print(user)

            if user is not None:
                login(request, user)
                return redirect(reverse('core:home'))
            return render(request, "users/signup.html", {"form": form})
