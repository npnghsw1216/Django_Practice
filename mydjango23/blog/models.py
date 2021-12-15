from django.db import models
from django.urls import reverse


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


class Post(TimestampedModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="blog/post/%Y/%m/%d")
    Tag_set = models.ManyToManyField('Tag', blank=True)
    status = models.CharField(
        max_length=1,
        # FIXME: 장고 3에서 추가된 TextChoices 기능을 활용
        choices=[
            ('D', '초안'),  # Draft // DB 저장값, Label
            ('P', '공개'),  # Published
        ],
        db_index=True,
        default='D',
    )  # 비공개, 삭제,

    def __str__(self):
        return self.title

    # post detail 주소 문자열을 반환
    # detail 페이즈를 구현하자마자, 즛기 아래 메서드를 구현합니다.
    def get_absolute_url(self) -> str:
        return reverse("blog:post_detail", args=[self.pk])

    class Meta:
        ordering = ["-id"]


class Comment(TimestampedModel):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
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
