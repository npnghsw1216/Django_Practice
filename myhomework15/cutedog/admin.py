from django.contrib import admin
from cutedog.models import Video


class VideoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Video, VideoAdmin)
