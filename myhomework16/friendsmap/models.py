from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=200)
    image_file = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
