from ...vadmin.op_drf.models import BaseModel
from django.db.models import CharField


class QuestionBroad(BaseModel):
    question_name = CharField(max_length=8, verbose_name='问题大类名称', help_text='问题大类名称')

    class Meta:
        verbose_name = '问题大类'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.question_name}'
