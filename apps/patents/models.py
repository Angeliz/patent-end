import uuid

from django.db import models

class Patents(models.Model):
    patents_id = models.UUIDField(primary_key=True,
                               default=uuid.uuid4,
                               editable=False,
                               verbose_name='一个专利的id',
                               help_text='专利的唯一id，pk')

    # patents_in_project = models.ForeignKey(Projects, on_delete=models.SET_NULL, blank=True, null=True, verbose_name='所属项目',
    #                                     help_text='一个专利所属的项目')

    patents_name = models.TextField(verbose_name="专利名", help_text="专利名")
    patents_publication_number = models.TextField(verbose_name="公开号", help_text="公开号")
    patents_publication_date = models.TextField(verbose_name="公开日", help_text="公开日")
    patents_applicant = models.TextField(verbose_name="申请人", help_text="申请人")
    patents_inventor = models.TextField(verbose_name="发明人", help_text="发明人")
    patents_ipc = models.TextField(verbose_name="IPC", help_text="IPC")
    patents_abstract = models.TextField(verbose_name="摘要", help_text="专利摘要")
    patents_area = models.TextField(verbose_name='地区', help_text='项目所属地区')
    patents_field = models.TextField(verbose_name='领域', help_text='项目所属领域')
    patents_score = models.FloatField(verbose_name='评分', help_text='项目评分')

