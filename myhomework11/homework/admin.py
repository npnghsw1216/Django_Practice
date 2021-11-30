from django.contrib import admin
from homework.models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ["dog_name", "dog_size", "dog_origin", "dog_explain", "dog_caution", "created_at"]
    search_fields = ["dog_name"]

admin.site.register(Post, PostAdmin)
