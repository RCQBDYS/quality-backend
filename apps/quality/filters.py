import django_filters

from .models import Questions
from .models import QuestionBroad
from .models import QuestionOrigin
from .models import QuestionLevel


class QuestionsFilter(django_filters.rest_framework.FilterSet):
    # 控制搜索时搜索方式：模糊还是准确
    question_title = django_filters.CharFilter(lookup_expr='icontains')
    machine_category = django_filters.CharFilter(lookup_expr='icontains')
    question_description = django_filters.CharFilter(lookup_expr='icontains')
    duty_person = django_filters.CharFilter(lookup_expr='icontains')
    question_slender = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Questions
        exclude = ('description', 'creator', 'modifier')


class QuestionBroadFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = QuestionBroad
        exclude = ('description', 'creator', 'modifier')


class QuestionLevelFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = QuestionLevel
        exclude = ('description', 'creator', 'modifier')


class QuestionOriginFilter(django_filters.rest_framework.FilterSet):

    class Meta:
        model = QuestionOrigin
        exclude = ('description', 'creator', 'modifier')

