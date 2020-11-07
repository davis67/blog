from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("signup", views.SignUpView.as_view(), name="signup"),
    path("login", views.LoginView.as_view(), name="login"),
    path("logout", views.log_out, name="logout"),
    path("add-profile", views.AddProfileView.as_view(),
         name="add-profile-picture"),
]
