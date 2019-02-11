from django.db import models

# Create your models here.


class Bridge(models.Model):
    touch_key = models.CharField(max_length=20,verbose_name="已登入的 key",default="")

    class Meta:
        verbose_name = "登录者 key"
        verbose_name_plural = verbose_name