from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views, admin

urlpatterns = [
    path("admin/", admin.site.urls),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)