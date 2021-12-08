from django.urls import path

from constellation import views

app_name = "constellation"

urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("<int:pk>/", views.post_detail, name="post_detail"),
]

