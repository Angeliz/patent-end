from django.db import models

# Create your models here.
import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.postgres.fields import JSONField, ArrayField
# Create your models here.


class Users(AbstractUser):
    # user_id = models.UUIDField(primary_key=True,
    #                             default=uuid.uuid4,
    #                             editable=False,
    #                             verbose_name='用户的id',
    #                             help_text='用户的唯一id，pk')

    # user_name = models.TextField(verbose_name="用户名", help_text="用户名")
    # user_password = models.TextField(verbose_name='密码', help_text='密码')
    user_type = models.TextField(verbose_name='用户类型', help_text='专家（1）、商家（2）或普通用户（3）', blank=False)
    user_email = models.TextField(verbose_name='邮箱', help_text='用户邮箱')
    user_phone_number = models.TextField(verbose_name='电话', help_text='用户电话号码')
    user_address = models.TextField(verbose_name='地址', help_text='地址')
    user_info = models.TextField(verbose_name='介绍', help_text='用户介绍', blank=True)










