from django.contrib import admin

from constellation.models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
