from django.db import models


class Post(models.Model):
    title = models.CharField(max_length=20, db_index=True)
    description = models.TextField(blank=True)
    photo = models.ImageField()
    fortune = models.TextField(blank=True)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "별자리"
        verbose_name_plural = "별자리 목록"

