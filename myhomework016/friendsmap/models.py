from django.db import models
from imagekit.models import ImageSpecField


class Post(models.Model):  # pk: id(int)
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)
    image_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
