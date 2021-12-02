from django.contrib import admin
from dogtube.models import Video


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)
