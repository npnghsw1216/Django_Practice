from django.conf import settings
from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "카테고리"
        verbose_name_plural = "카테고리 목록"


class Shop(TimestampedModel):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, db_index=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="shop/shop/%Y/%m/%d", blank=True)
    tag_set = models.ManyToManyField('Tag', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-id"]
        verbose_name = "상점"
        verbose_name_plural = "상점 목록"


class Review(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-id"]
        verbose_name = "리뷰"
        verbose_name_plural = "리뷰 목록"


class Tag(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"
