import uuid

from django.db import models

from users.models import Users


class Orders(models.Model):
    orders_id = models.UUIDField(primary_key=True,
                                  default=uuid.uuid4,
                                  editable=False,
                                  verbose_name='一个订单的id',
                                  help_text='订单的唯一id，pk')

    orders_user = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='订单关联用户',
                                        help_text='订单关联用户')
    # orders_service = models.ForeignKey(Users, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='订单服务',
    #                                  help_text='订单接收者')

    orders_name = models.TextField(verbose_name="订单名", help_text="订单名")
    orders_state = models.IntegerField(verbose_name="订单状态", help_text="[订单状态]1=未完成；2=已完成")
    orders_method = models.IntegerField(verbose_name="评估方式", help_text="[评估方式]1=系统评估；2=用户自定义评估；3=专家人工评估；4=其他商家评估")
    orders_obj = models.IntegerField(verbose_name="评估对象", help_text="[评估对象]1=专利；2=机构")
    orders_create_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间戳', help_text='orders创建的时间戳')
    orders_update_at = models.DateTimeField(auto_now=True, verbose_name='更新时间戳', help_text='每次数据修改的时间戳')
