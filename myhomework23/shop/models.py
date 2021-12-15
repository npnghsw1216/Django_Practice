from django.db import models


class TimestampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(TimestampedModel):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["-id"]


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        ordering = ["-id"]


class Tag(TimestampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        ordering = ["name"]