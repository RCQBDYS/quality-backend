from .models.questionFollow import QuestionFollow
from .models.dailyProgress import DailyProgress
from ..vadmin.op_drf.serializers import CustomModelSerializer
from rest_framework import serializers


# ================================================= #
# ************** 每日维护管理 序列化器  ************** #
# ================================================= #
class DailyProgressSerializer(CustomModelSerializer):
    """
          项目管理 简单序列化器
    """
    # questionFollow = serializers.CharField(source='questionFollow.', read_only=True)

    class Meta:
        model = DailyProgress
        fields = '__all__'


class DailyProgressCreateUpdateSerializer(CustomModelSerializer):
    """
          项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = DailyProgress
        fields = '__all__'


# ================================================= #
# ************** 质量跟进管理 序列化器  ************** #
# ================================================= #
class QuestionFollowSerializer(CustomModelSerializer):
    """
      项目管理 简单序列化器
    """
    daily_follow = DailyProgressSerializer(many=True)

    class Meta:
        model = QuestionFollow
        fields = '__all__'


class QuestionFollowCreateUpdateSerializer(CustomModelSerializer):
    """
        项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = QuestionFollow
        fields = '__all__'


