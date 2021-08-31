from .filters import QuestionFollowFilter, DailyProgressFilter
from .models import QuestionFollow, DailyProgress
from .serializers import QuestionFollowSerializer, QuestionFollowCreateUpdateSerializer, DailyProgressSerializer, \
    DailyProgressCreateUpdateSerializer
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from apps.vadmin.permission.permissions import CommonPermission
from django.template import loader
from apps.vadmin.utils.response import SuccessResponse
from django.core.mail import send_mail
from application import settings
from apps.vadmin.permission.views import UserProfileModelViewSet, DeptModelViewSet
from apps.vadmin.permission.serializers import UserProfileSerializer, DeptSerializer
from rest_framework.request import Request
from apps.vadmin.op_drf.viewsets import CustomModelViewSet


class QuesFollowModelViewSet(CustomModelViewSet):
    """
    质量问题管理 的CRUD视图
    """
    queryset = QuestionFollow.objects.all()
    serializer_class = QuestionFollowSerializer  # 序列化器
    create_serializer_class = QuestionFollowCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = QuestionFollowCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = QuestionFollowFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('quesTitle',)  # 搜索
    ordering = ['-create_datetime']  # 默认排序

    # 修改问题状态
    def reset_status(self, request: Request, *args, **kwargs):
        instance = self.queryset.get(id=request.data.get('id'))
        instance.status = request.data.get('status')
        instance.save()
        serializer = self.get_serializer(instance)
        if hasattr(self, 'handle_logging'):
            self.handle_logging(request, instance=instance, *args, **kwargs)
        return SuccessResponse(serializer.data)

    def send_follow_email(self, request: Request, *args, **kwargs):
        # 获取内容新增问题id
        ID = request.data.get('id')
        href = request.data.get('url')
        instance = self.queryset.get(id=ID)
        serializer = self.get_serializer(instance)
        # 查询最新进度信息
        daily_follow = serializer.data['daily_follow'][-1]['content']
        # 查询责任科室、责任人、责任人邮箱
        officeId = serializer.data['officeId']
        deptInstance = DeptModelViewSet().queryset.get(id=officeId)
        deptSerializer = DeptSerializer(instance=deptInstance)
        deptName = deptSerializer.data['deptName']
        deptResponse = deptSerializer.data['leader']
        deptEmail = deptSerializer.data['email']
        # 查询下单人信息
        submitterId = serializer.data['submitter']
        submitter = UserProfileModelViewSet().queryset.get(id=submitterId)
        submitterSerializer = UserProfileSerializer(instance=submitter)
        submitterName = submitterSerializer.data['name']
        submitterEmail = submitterSerializer.data['email']
        # 查询跟进人信息
        followPersonId = serializer.data['followPerson']
        followPerson = UserProfileModelViewSet.queryset.get(id=followPersonId)
        followPersonSerializer = UserProfileSerializer(instance=followPerson)
        followPersonName = followPersonSerializer.data['name']
        followPersonEmail = followPersonSerializer.data['email']
        # 邮件推送内容
        content = {
            'url': href,
            'quesTitle': serializer.data['quesTitle'],
            'occurTime': serializer.data['occurTime'],
            'questionOrigin': serializer.data['questionOrigin'],
            'quesDescription': serializer.data['quesDescription'],
            'officeName': deptName,
            'resName': deptResponse,
            'followName': followPersonName,
            'submitterName': submitterName,
            'dailyFollow': daily_follow,
            'userOne': followPersonName,
            'userTow': submitterName
        }
        # 邮箱拼接
        if deptEmail is None:
            receiveList = [submitterEmail, followPersonEmail]
        else:
            receiveList = deptEmail.split(',')
            receiveList.append(submitterEmail)
            receiveList.append(followPersonEmail)

        # 填充内容
        html = loader.get_template('qualityFollow.html')
        html_content = html.render(content)
        send_mail(subject=serializer.data['quesTitle'], message='', from_email=settings.EMAIL_HOST_USER,
                  recipient_list=receiveList,
                  html_message=html_content)
        return SuccessResponse()


class DailyProgressModelViewSet(CustomModelViewSet):
    """
    每日维护信息 的CRUD视图
    """
    queryset = DailyProgress.objects.all()
    serializer_class = DailyProgressSerializer  # 序列化器
    create_serializer_class = DailyProgressCreateUpdateSerializer  # 创建/更新时的列化器
    update_serializer_class = DailyProgressCreateUpdateSerializer  # 创建/更新时的列化器
    filter_class = DailyProgressFilter  # 过滤器
    extra_filter_backends = [DataLevelPermissionsFilter]  # 数据权限类，不需要可注释掉
    update_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    destroy_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    create_extra_permission_classes = (CommonPermission,)  # 判断用户是否有这条数据的权限
    search_fields = ('content',)  # 搜索
    ordering = ['-create_datetime']

# class ReportModelViewSet(ModelViewSet):
#     """
#     报表信息 的CRUD视图
#     """
#     queryset = QuestionFollow.objects.all()
