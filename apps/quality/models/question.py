from ...vadmin.op_drf.models import CoreModel
from django.db.models import CharField, IntegerField, DateTimeField, TextField, ManyToManyField, ForeignKey, CASCADE


class Questions(CoreModel):
    # 质量管理model
    question_title = CharField(max_length=128, verbose_name='问题主题', help_text='问题主题')
    machine_category = CharField(max_length=32, verbose_name='机型类别', help_text='机型类别', null=True)
    machine_name = CharField(max_length=32, verbose_name='机器名称', help_text='机器名称', null=True)
    machine_num = IntegerField(verbose_name='涉及台数', help_text='涉及台数', null=True)
    question_broad = CharField(max_length=32, verbose_name='问题大类', help_text='问题大类', null=True)
    question_slender = CharField(max_length=32, verbose_name='问题细类', help_text='问题细类', null=True)
    # 责任部门
    duty_dep_id = IntegerField(verbose_name='部门id', help_text='部门id')
    # 责任科室
    duty_office_id = IntegerField(verbose_name='科室id', help_text='科室id', null=True)
    duty_person = CharField(max_length=8, verbose_name='责任人', help_text='责任人')
    occur_time = DateTimeField(verbose_name='发生时间', help_text='发生时间')
    number = IntegerField(verbose_name='故障数量', help_text='故障数量', null=True)
    question_level = CharField(max_length=8, verbose_name='重要程度', help_text='重要程度')
    question_origin = CharField(max_length=8, verbose_name='问题来源', help_text='问题来源')
    # 关闭与否
    title_status = CharField(max_length=8, verbose_name='问题状态', help_text='问题状态')
    black_point = CharField(max_length=8, verbose_name='黑点', help_text='黑点', null=True)
    question_description = CharField(max_length=128, verbose_name='问题描述', help_text='问题描述')
    question_schedule = CharField(max_length=128, verbose_name='问题进度', help_text='问题进度')
    attachment = TextField(verbose_name='附件', help_text='附件', null=True)
    # w

    class Meta:
        verbose_name = '质量管理'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.question_title}"


