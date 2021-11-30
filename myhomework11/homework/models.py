from django.db import models


class Post(models.Model):
    # list_display = ["dog_name", "dog_size", "dog_origin", "dog_explain", "dog_caution", "created_at"]
    # search_fields = ["dog_name"]
    dog_name = models.CharField(max_length=20)
    dog_size = models.CharField(max_length=20)
    dog_origin = models.CharField(max_length=20)
    dog_explain = models.TextField()
    dog_caution = models.TextField()
    #  upload_to
    #  - 문자열 : 파일이 저장되는 폴더의 경로
    photo = models.ImageField(blank=True)  # , upload_to='blog/post/%Y/%m/%d/%H')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)