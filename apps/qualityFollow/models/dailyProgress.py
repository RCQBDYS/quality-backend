from ...vadmin.op_drf.models import CoreModel
from django.db.models import CharField, ManyToManyField, IntegerField, TextField, ForeignKey, CASCADE


class DailyProgress(CoreModel):
    officeId = IntegerField(verbose_name='分析科室', help_text='分析科室')
    userId = IntegerField(verbose_name='用户名', help_text='用户名')
    status = CharField(max_length=32, verbose_name='维护状态', help_text='维护状态')
    content = TextField(verbose_name='每日答复', help_text='每日答复')
    fileId = IntegerField(verbose_name='文件id', help_text='文件id', null=True, blank=True)
    fileName = CharField(max_length=128, verbose_name='文件名称', help_text='文件名称', null=True, blank=True)
    questionFollow = ForeignKey(to='qualityFollow.QuestionFollow', verbose_name='所属跟进问题', on_delete=CASCADE,
                                db_constraint=False, null=True, blank=True, related_name='daily_follow')
    files = ManyToManyField(to='system.SaveFile', verbose_name='预留多文件上传', help_text='预留多文件上传', null=True, blank=True)

    class Meta:
        verbose_name = '每日维护'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f"{self.content}"
