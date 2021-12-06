
from django.contrib import admin
from django.urls import path
from delicious.views import shop_list, shop_detail, shop_new_1, shop_new

app_name = "delicious"  # namespace

urlpatterns = [
    path('', shop_list, name='shop_list'),
    path('<int:pk>/', shop_detail, name='shop_detail'),
    path('new1/', shop_new_1),
    path('new/', shop_new),
]
