import django_filters

from .models import Questions
from .models import QuestionBroad
from .models import QuestionOrigin
from .models import QuestionLevel


class QuestionsFilter(django_filters.rest_framework.FilterSet):

    question_title = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Questions
        exclude = ('description', 'creator', 'modifier')


class QuestionBroadFilter(django_filters.rest_framework.FilterSet):
    question_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = QuestionBroad
        exclude = ('description', 'creator', 'modifier')


class QuestionLevelFilter(django_filters.rest_framework.FilterSet):
    question_level = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = QuestionLevel
        exclude = ('description', 'creator', 'modifier')


class QuestionOriginFilter(django_filters.rest_framework.FilterSet):
    question_origin = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = QuestionOrigin
        exclude = ('description', 'creator', 'modifier')

