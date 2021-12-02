from django.db import models


class Video(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    video_file = models.FileField()
    thumbnail_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)