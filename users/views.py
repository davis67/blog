from django.shortcuts import render
from django.views import View
from . import forms, models


class SignUpView(View):
    def get(self, request):
        form = forms.SignUpForm()
        return render(request, "users/signup.html", {"form": form})
