from django.urls import path
from . import views

app_name = "posts"

urlpatterns = [
    path("add/", views.PostCreate.as_view(), name="post-create"),
    path("<int:pk>/", views.PostDetail.as_view(), name="detail"),
    path("edit/<int:pk>/", views.PostUpdate.as_view(), name="post-update"),
    path("delete/<int:pk>/", views.PostDelete.as_view(), name="post-delete"),
    path("reply/<int:pk>/", views.AddReply.as_view(), name="add-reply"),
    path("comment/<int:pk>/", views.AddComment.as_view(), name="add-comment")
]
