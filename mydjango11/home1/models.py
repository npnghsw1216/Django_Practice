from django.db import models

class Profile(models.Model):

    first_name = models.CharField(max_length=100, verbose_name="이름")
    last_name = models.CharField(max_length=100, verbose_name="성")
    address = models.CharField(max_length=100, verbose_name="주소")
    e_mail = models.CharField(max_length=100, verbose_name="이메일 주소")
    mobile = models.CharField(max_length=11, verbose_name="연락처")
    comment = models.TextField(max_length=100, verbose_name="소개")
    date = models.DateTimeField(verbose_name="날 짜")