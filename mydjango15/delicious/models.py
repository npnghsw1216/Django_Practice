from django.db import models
from django.core.validators import RegexValidator

class Shop(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(blank=True)
    address = models.CharField(max_length=100)
    # TODO : GeoDjango의 PointField를 사용
    latitude = models.FloatField(verbose_name="위도")
    longitude = models.FloatField(verbose_name="경도")
    # TODO : 전화번호 값인지 여부를 체킹
    telephone = models.CharField(max_length=15,
                                 validators=[
                                     RegexValidator(r"^\d{3,4}-?\ㅇ{4}-?\ㅇ{4}$",         # {3,4}-> 숫자가 연속으로 세번에서 네번
                                                    message="전화번호를 입력해주세요"),      # -? - 가 있을수도 있고 없을 수도 있다
                                 ])
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)