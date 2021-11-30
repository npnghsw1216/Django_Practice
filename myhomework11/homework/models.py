from django.db import models


class Post(models.Model):
    author_name = models.CharField(max_length=20)
    title = models.CharField(max_length=200)
    content = models.TextField()
    #  upload_to
    #  - 문자열 : 파일이 저장되는 폴더의 경로
    photo = models.ImageField(blank=True)  # , upload_to='blog/post/%Y/%m/%d/%H')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)