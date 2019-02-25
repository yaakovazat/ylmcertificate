from django.db import models

# Create your models here.
class Order(models.Model):
    data_updated = models.CharField(max_length=40,verbose_name="更新时间", default="")
    ID = models.CharField(primary_key=True, max_length=40,verbose_name="订单编号", default="")
    order_name = models.CharField(max_length=50, verbose_name="收件人", default="")
    order_phone = models.CharField(max_length=20, verbose_name="手机号", default="")
    order_group = models.CharField(max_length=40, verbose_name="组别",default="")
    order_detail = models.CharField(max_length=200, verbose_name="商品描述", default="")
    express = models.CharField(max_length=20, verbose_name="快递公司", default="中通快递")
    express_id = models.CharField(max_length=50, verbose_name="快递单号", default="")
    order_status = models.CharField(max_length=40, verbose_name="订单状态", default="正常")
    order_get_time = models.CharField(max_length=30,verbose_name="下单日期", default="")
    order_done_time =models.CharField(max_length=30, verbose_name="审核日期", default="")
    external_ID = models.CharField(max_length=30, verbose_name="外部订单号", default="")


    class Meta:
        verbose_name = "订单详情"
        verbose_name_plural = verbose_name