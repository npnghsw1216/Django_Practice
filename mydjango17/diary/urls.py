from django.urls import path

from diary import views

app_name = "diary"

urlpatterns = [
    path("", views.post_list, name="post_list"),
]
