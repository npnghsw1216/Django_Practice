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
        ordering = ["name"]  # 내림차순보단 가, 나, 다 순으로 정렬


class Shop(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="shop/shop/%Y/%m/%d")
    Tag_set = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(
        max_length=1,
        choices=[
            ('D', '초안'),  # Draft // DB 저장값, Label
            ('P', '공개'),  # Published
        ],
        db_index=True,
        default='D',
    )  # 비공개, 삭제,

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-id"]


class Comment(TimestampedModel):
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    message = models.TextField()

    def __str__(self):
        return self.message

    class Meta:
        ordering = ["-id"]


class Tag(TimestampedModel):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

