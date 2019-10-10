from django.db import models
from django.conf import settings
from django.utils import timezone
import os
from uuid import uuid4


class Shop(models.Model):
    def date_upload_to(self, filename):
        # upload_to="%Y/%m/%d" 처럼 날짜로 세분화
        ymd_path = timezone.now().strftime('%Y/%m/%d') 
        # 길이 32 인 uuid 값
        uuid_name = uuid4().hex
        # 확장자 추출
        extension = os.path.splitext(filename)[-1].lower()
        # 결합 후 return
        return '/'.join([
            ymd_path,
            uuid_name + extension,
        ])
    name = models.CharField(
        max_length=128,
        verbose_name="상품명")
    photoUrl = date_upload_to
    photo = models.ImageField(upload_to=photoUrl)



    def __str__(self):
        return self.name

    class Meta:
        db_table = 'trackline_shop'
        verbose_name = '상품'
        verbose_name_plural = '상품들'