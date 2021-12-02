from django.contrib import admin
from blog.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "author_name", "created_at"]
    search_fields = ["title"]

admin.site.register(Post, PostAdmin)
