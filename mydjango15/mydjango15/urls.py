
from django.contrib import admin
from django.urls import path, include
from delicious.views import shop_list, shop_detail, shop_new_1, shop_new

urlpatterns = [
    path('admin/', admin.site.urls),
    path('delicious/', include('delicious.urls')),
]

