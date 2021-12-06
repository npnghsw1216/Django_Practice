from django.contrib import admin
from blog.models import Post, Comment, Tag


# 장식자 이용하기
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
     pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
     list_display = ["pk", "post", "message", "created_at"]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
     pass