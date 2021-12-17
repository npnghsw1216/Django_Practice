from django.urls import path

from accounts import views

app_name = "accounts"

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.signup, name='login'),
    path('profile/', views.signup, name='profile'),
    path('logout/', views.signup, name='logout'),
]