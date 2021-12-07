from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # 추상 클래스로서, DB 테이블이 생기지 않는다. (부모로서만 존재)


class Post(TimeStampedModel):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="news/post/%Y/%m/%d") # 연, 월, 일로 나눠서 저장
    tag_set = models.ManyToManyField("Tag", blank=True)

    def __str__(self) -> str:
        return self.title

    class Meta:
        verbose_name = "포스팅"
        verbose_name_plural = "포스팅 목록"


class Comment(TimeStampedModel):
    # 외래키 : 정수값
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    # 내부적으로 만들어 주는 것 post_id
    author_name = models.CharField(max_length=20)
    message = models.TextField()

    class Meta:
        verbose_name = "댓글"
        verbose_name_plural = "댓글 목록"


class Tag(TimeStampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name = "태그"
        verbose_name_plural = "태그 목록"

