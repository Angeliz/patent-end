import uuid

from django.db import models

# Create your models here.
from users.models import Users
from patents.models import Patents


class Projects(models.Model):
    projects_id = models.UUIDField(primary_key=True,
                                   default=uuid.uuid4,
                                   editable=False,
                                   verbose_name='一个projects的id',
                                   help_text='projects的唯一id，pk')

    # projects_user = models.ForeignKey(Users, on_delete=models.CASCADE)
    project_patents = models.ForeignKey(Patents, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='包含专利',
                                        help_text='一个项目包含的专利')

    projects_name = models.TextField(verbose_name="项目名", help_text="一个项目的项目名")
    projects_info = models.TextField(verbose_name='介绍', help_text='一个项目的介绍信息')
    projects_type = models.TextField(verbose_name='类型', help_text='项目类型')
    projects_area = models.TextField(verbose_name='地区', help_text='项目所属地区')
    projects_field = models.TextField(verbose_name='领域', help_text='项目所属领域')
    projects_background = models.TextField(verbose_name='背景', help_text='项目背景')
    projects_feature = models.TextField(verbose_name='特点', help_text='项目特点')
    projects_score = models.FloatField(verbose_name='评分', help_text='项目评分')

