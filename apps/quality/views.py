from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission
from .filters import QuestionsFilter, QuestionLevelFilter, QuestionBroadFilter, QuestionOriginFilter
from .models.question import Questions
from .models.question_level import QuestionLevel
from .models.question_broad import QuestionBroad
from .models.question_origin import QuestionOrigin
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from .serializers import QuestionSerializer, QuestionCreateUpdateSerializer, QuestionLevelSerializer, QuestionLevelUpdateSerializer, \
    QuestionBroadSerializer, QuestionBroadUpdateSerializer, QuestionOriginSerializer, QuestionOriginUpdateSerializer


class QuestionsModelViewSet(CustomModelViewSet):
    queryset = Questions.objects.all()
    # 序列化器
    serializer_class = QuestionSerializer
    # 创建/更新序列化器
    create_serializer_class = QuestionCreateUpdateSerializer
    update_serializer_class = QuestionCreateUpdateSerializer
    # 过滤器
    filter_class = QuestionsFilter
    # 判断用户是否拥有这条数据的权限
    extra_filter_backends = [DataLevelPermissionsFilter]
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)
    # 搜索
    search_field_data = 'question_title'
    # 已创建时间进行数据的排序
    ordering = ['-occur_time']


class QLModelViewSet(CustomModelViewSet):

    queryset = QuestionLevel.objects.all()
    # 序列化器
    serializer_class = QuestionLevelSerializer
    # 创建/更新序列化器
    create_serializer_class = QuestionLevelUpdateSerializer
    update_serializer_class = QuestionLevelUpdateSerializer
    # 过滤器
    filter_class = QuestionLevelFilter
    update_extra_permission_classes = (CommonPermission,)
    destroy_extra_permission_classes = (CommonPermission,)
    create_extra_permission_classes = (CommonPermission,)


class QBModelViewSet(CustomModelViewSet):
    queryset = QuestionBroad.objects.all()
    # 序列化器
    serializer_class = QuestionBroadSerializer
    # 创建/更新序列化器
    create_serializer_class = QuestionBroadUpdateSerializer
    update_serializer_class = QuestionBroadUpdateSerializer
    # 过滤器
    filter_class = QuestionBroadFilter


class QOModelViewSet(CustomModelViewSet):
    queryset = QuestionOrigin.objects.all()
    # 序列化器
    serializer_class = QuestionOriginSerializer
    # 创建/更新序列化器
    create_serializer_class = QuestionOriginUpdateSerializer
    update_serializer_class = QuestionOriginUpdateSerializer
    # 过滤器
    filter_class = QuestionOriginFilter

