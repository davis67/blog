from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("add", views.PostCreate.as_view(), name="post-create"),
    path("<int:pk>", views.PostDetail.as_view(), name="detail")
]
