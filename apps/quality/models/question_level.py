from ...vadmin.op_drf.models import BaseModel
from django.db.models import CharField


class QuestionLevel(BaseModel):
    question_level = CharField(max_length=8, verbose_name='问题等级', help_text='问题等级')

    class Meta:
        verbose_name = '问题等级'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'{self.question_level}'
