"""mydjango15 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from delicious.views import shop_list, shop_detail, shop_new_1, shop_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delicious/', shop_list),
    path('delicious/<int:pk>/', shop_detail),
    path('delicious/new1/', shop_new_1),
    path('delicious/new/', shop_new),
]
