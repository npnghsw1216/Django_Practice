from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimeStampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]


class Shop(TimeStampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True,)
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-id"]


class Review(TimeStampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    name = models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-id"]


class Tag(TimeStampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]

