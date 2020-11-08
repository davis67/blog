from django.contrib import messages
from django.urls import reverse_lazy
from django.shortcuts import redirect, redirect
from django.contrib.auth.mixins import UserPassesTestMixin, LoginRequiredMixin
from django.http import HttpResponseRedirect


class MustAddProfilePictureAfterSignUp(UserPassesTestMixin):
    permission_denied_message = "You must add a Profile Picture to continue"

    def test_func(self):
        if self.request.user.is_authenticated is False:
            return True
        return bool(self.request.user.avatar) is True

    def handle_no_permission(self):
        return redirect("users:add-profile-picture")


class LoggedOutOnlyView(UserPassesTestMixin):
    def test_func(self):
        return not self.request.user.is_authenticated

    def handle_no_permission(self):
        messages.error(self.request, "You must log out to access this page")
        return redirect('core:home')


class LoggedInOnlyView(LoginRequiredMixin):
    login_url = reverse_lazy("users:login")
