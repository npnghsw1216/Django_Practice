from django.contrib import admin

from news.models import Post, Comment, Tag

admin.site.register(Post)
# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Comment)
# class CommentAdmin(admin.ModelAdmin):
#     pass
#
#
# @admin.register(Tag)
# class TagAdmin(admin.ModelAdmin):
#     pass
