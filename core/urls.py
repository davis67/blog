from django.urls import path
from django.conf.urls import url
from posts import views as post_views

app_name = "core"

urlpatterns = [
    path("<slug:category>/", post_views.HomeView.as_view(), name="home"),
    path("", post_views.HomeView.as_view(), name="home"),
]
