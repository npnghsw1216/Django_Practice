from django.db import models

class Order(models.Model):
    name = models.CharField(max_length=100, verbose_name="이름")
    address = models.CharField(max_length=100, verbose_name="주소")
    mobile = models.CharField(max_length=11, verbose_name="연락처")
    menus = models.TextField(verbose_name="주문 메뉴들") # FK를 쓰는 게 적절