from django.db import models

# Create your models here.

class Agent(models.Model):
    name = models.CharField(max_length=40,verbose_name="姓名", default="")
    telephone = models.CharField(max_length=11, verbose_name="手机号", default="")
    key = models.CharField(max_length=20, verbose_name="授权码", default="")
    idcard = models.CharField(max_length=40, verbose_name="身份证号",default="")
    wechat = models.CharField(max_length=20, verbose_name="微信号", default="")
    email = models.EmailField(max_length=20, verbose_name="邮箱", default="")
    address = models.CharField(max_length=100, verbose_name="代理地址", default="")
    profession = models.CharField(max_length=20, verbose_name="代理职业", default="")
    work_place = models.CharField(max_length=40, verbose_name="工作单位", default="")
    message = models.CharField(max_length=500,verbose_name="用户留言信息", default="")
    certificate =models.CharField(max_length=30, verbose_name="授权书", default="")



    class Meta:
        verbose_name = "代理钥匙"
        verbose_name_plural = verbose_name
