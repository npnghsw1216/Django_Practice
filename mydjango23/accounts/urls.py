from django.urls import path
from accounts import views

app_name = "accounts"

urlpatterns = [
    path("profile.png", views.profile_image, name="profile_image"),
    path("login/", views.login, name="login"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
    path("logout/", views.logout, name="logout"),
]
