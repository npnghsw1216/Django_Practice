from django.urls import path

from news import views

app_name = "news"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
    path("tags/<str:tag_name>/", views.tag_detail, name="tag_detail"),
]
