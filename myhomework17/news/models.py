from django.db import models


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        # 추상 클래스로서, DB 테이블이 생기지 않는다.
        # 부모로서만 존재해서


class Post(TimeStampedModel):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    photo = models.ImageField(upload_to="news/post/%Y/%m/%d")  # 연, 월, 일로 나눠서 저장

    def __str__(self) -> str:
        return self.title


class Comment(TimeStampedModel):

    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name =models.CharField(max_length=20)
    message = models.TextField()

    def __str__(self) -> str:
        return self.title


class Tag(TimeStampedModel):
    name = models.CharField(max_length=200, db_index=True)

    def __str__(self) -> str:
        return self.title


