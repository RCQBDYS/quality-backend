from ...vadmin.op_drf.models import CoreModel
from django.db.models import CharField, DateField, IntegerField, TextField, ManyToManyField


class QuestionFollow(CoreModel):
    questionOrigin = CharField(max_length=128, verbose_name='问题来源', help_text='问题来源')
    occurTime = DateField(verbose_name='发生时间', help_text='发生时间')
    officeId = IntegerField(verbose_name='科室', help_text='科室')
    resPerson = CharField(max_length=64, verbose_name='责任人', help_text='责任人')
    followPerson = IntegerField(verbose_name='跟进人', help_text='跟进人')
    quesTitle = CharField(max_length=128, verbose_name='问题主题', help_text='问题主题')
    quesDescription = TextField(verbose_name='问题描述', help_text='问题描述')
    submitter = IntegerField(verbose_name='下单人', help_text='下单人')
    fileId = IntegerField(verbose_name='文件id', help_text='文件id', null=True, blank=True)
    fileName = CharField(max_length=128, verbose_name='文件名称', help_text='文件名称', null=True, blank=True)
    relate = CharField(max_length=128, verbose_name='是否涉及其他产品', help_text='是否涉及其他产品', null=True, blank=True)
    causeAnalysis = TextField(verbose_name='原因分析', help_text='原因分析')
    tempSolution = TextField(verbose_name='临时解决方案', help_text='临时解决方案')
    longSolution = TextField(verbose_name='长期解决方案', help_text='长期解决方案')
    alternative = TextField(verbose_name='预防措施', help_text='预防措施')
    detailPlan = TextField(verbose_name='详细计划', help_text='详细计划')
    status = IntegerField(verbose_name='问题状态', help_text='问题状态')
    # relateUser = ManyToManyField(to='permission.UserProfile', verbose_name='预留指派责任人', help_text='预留指派责任人',
    #                              db_constraint=False)
    files = ManyToManyField(to='system.SaveFile', verbose_name='预留多文件上传', help_text='预留多文件上传', db_constraint=False,
                               null=True, blank=True)

    class Meta:
        verbose_name = '质量跟进'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.quesTitle}"
