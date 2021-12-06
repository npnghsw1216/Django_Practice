from django.db import models


class Post(models.Model):  # pk: id(int)
    title = models.CharField(max_length=200, db_index=True)
    content = models.TextField()
    tag_set = models.ManyToManyField('Tag', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # 인스턴스에 대한 문자열 표현을 기대
    # post.title
    # print(post)
    # 내부적으로 post.__str__을 찾아서 호출해서 반환값을 출력
    # print(post.__str__())

    def __str__(self) -> str:
        return self.title


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self) -> str:
        return self.name


