from ...vadmin.op_drf.models import BaseModel
from django.db.models import CharField


class QuestionOrigin(BaseModel):
    question_origin = CharField(max_length=8, verbose_name='问题来源', help_text='问题来源')

    class Meta:
        verbose_name = '问题来源'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.question_origin}'
