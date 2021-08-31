import django_filters

from .models import QuestionFollow
from .models import DailyProgress


class QuestionFollowFilter(django_filters.rest_framework.FilterSet):
    quesTitle = django_filters.CharFilter(lookup_expr='icontains')
    resPerson = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = QuestionFollow
        exclude = ('description', 'creator', 'modifier')


class DailyProgressFilter(django_filters.rest_framework.FilterSet):
    content = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = DailyProgress
        exclude = ('description', 'creator', 'modifier')
