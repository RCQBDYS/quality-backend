from rest_framework.request import Request

from application import settings
from apps.vadmin.op_drf.viewsets import CustomModelViewSet
from apps.vadmin.permission.permissions import CommonPermission
from .filters import QuestionsFilter, QuestionLevelFilter, QuestionBroadFilter, QuestionOriginFilter
from .models.question import Questions
from .models.question_level import QuestionLevel
from .models.question_broad import QuestionBroad
from .models.question_origin import QuestionOrigin
from apps.vadmin.op_drf.filters import DataLevelPermissionsFilter
from .serializers import QuestionSerializer, QuestionCreateUpdateSerializer, QuestionLevelSerializer, \
    QuestionLevelUpdateSerializer, \
    QuestionBroadSerializer, QuestionBroadUpdateSerializer, QuestionOriginSerializer, QuestionOriginUpdateSerializer
from django.core.mail import send_mail
from apps.vadmin.utils.response import SuccessResponse


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
    ordering = ['-create_datetime']

    def send_email(self, request: Request):
        # 从url中获取参数
        ID = request.data.get('questionId')
        receiveList = request.data.get('receiveList')
        href = request.data.get('href')
        # 根据id值查询具体信息
        instance = self.queryset.get(id=ID)
        serializer = self.get_serializer(instance)
        print(receiveList)
        # 发送html格式内容
        # html_name = 'email.html'
        # email_html = loader.get_template(html_name)
        # html_content = email_html.render(content)
        email_message = """
        <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>售后问题</title>
</head>
<body>
<div id="content">
    <table width="80%" border="0" cellspacing="0" cellpadding="0" align="center">
        <tr>
            <td align="center" class="biaoti" height="60">售后问题</td>
        </tr>
        <tr>
            <td align="right" height="25">""" + serializer.data['create_datetime'] + """</td>
        </tr>
    </table>

    <table width="80%" border="0" cellspacing="1" cellpadding="4" bgcolor="#cccccc" class="tabtop13" align="center">
        <tr>
            <td colspan="2" class="btbg font-center titfont">问题主题</td>
            <td colspan="4">""" + serializer.data['question_title'] + """</td>
            <td colspan="2" class="btbg font-center titfont">责任人</td>
            <td colspan="4">""" + serializer.data['duty_person'] + """</td>
        </tr>
        <tr>
            <td colspan="2" class="btbg font-center titfont">创建时间</td>
            <td colspan="4">""" + serializer.data['occur_time'] + """</td>
            <td colspan="2" class="btbg font-center titfont">问题来源</td>
            <td colspan="4">""" + serializer.data['question_origin'] + """</td>
        </tr>
        <tr>
            <td colspan="2" rowspan="5" class="btbg font-center titfont">问题描述</td>
            <td colspan="10" rowspan="5">""" + serializer.data['question_description'] + """</td>
        </tr>
        <tr>
            <td colspan="2" rowspan="5" class="btbg font-center titfont">问题进度</td>
            <td colspan="10" rowspan="5">""" + serializer.data['question_schedule'] + """</td>
        </tr>
    </table>
    <span>详情请见""" + href + """</span>
</div>
</body>
</html>
<style>
    

    .tabtop13 td {
        background-color: #ffffff;
        height: 25px;
        line-height: 150%;
    }

    .font-center {
        text-align: center
    }

    .btbg {
        background: #e9faff !important;
    }

    .btbg1 {
        background: #f2fbfe !important;
    }

    .btbg2 {
        background: #f3f3f3 !important;
    }

    .biaoti {
        font-family: 微软雅黑;
        font-size: 26px;
        font-weight: bold;
        border-bottom: 1px dashed #CCCCCC;
        color: #255e95;
    }

    .titfont {

        font-family: 微软雅黑;
        font-size: 16px;
        font-weight: bold;
        color: #255e95;
        background-color: #e9faff;
    }

    .tabtxt2 {
        font-family: 微软雅黑;
        font-size: 14px;
        font-weight: bold;
        text-align: right;
        padding-right: 10px;
        color: #327cd1;
    }

    .tabtxt3 {
        font-family: 微软雅黑;
        font-size: 14px;
        padding-left: 15px;
        color: #000;
        margin-bottom: 10px;
        line-height: 20px;
    }
</style>
        """
        send_mail(subject=serializer.data['question_title'], message=serializer.data['question_description'],
                  from_email=settings.EMAIL_HOST_USER, recipient_list=receiveList, html_message=email_message)

        return SuccessResponse(msg='邮件已发送成功！')


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
