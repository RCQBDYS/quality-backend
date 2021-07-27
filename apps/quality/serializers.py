
from .models.question import Questions
from .models.question_broad import QuestionBroad
from .models.question_origin import QuestionOrigin
from .models.question_level import QuestionLevel
from ..vadmin.op_drf.serializers import CustomModelSerializer

# ================================================= #
# ************** 售后问题管理 序列化器  ************** #
# ================================================= #


class QuestionSerializer(CustomModelSerializer):
    """
    项目管理 简单序列化器
    """

    class Meta:
        model = Questions
        fields = '__all__'


class QuestionCreateUpdateSerializer(CustomModelSerializer):
    """
    项目管理 创建/更新时的列化器
    """

    # 此处可写定制的 创建/更新 内容
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = Questions
        fields = '__all__'


# ================================================= #
# ************** 问题等级 序列化器  ************** #
# ================================================= #


class QuestionLevelSerializer(CustomModelSerializer):

    class Meta:
        model = QuestionLevel
        fields = '__all__'


class QuestionLevelUpdateSerializer(CustomModelSerializer):
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = QuestionLevel
        fields = '__all__'

# ================================================= #
# ************** 问题大类 序列化器  ************** #
# ================================================= #

class QuestionBroadSerializer(CustomModelSerializer):

    class Meta:
        model = QuestionBroad
        fields = '__all__'


class QuestionBroadUpdateSerializer(CustomModelSerializer):
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = QuestionBroad
        fields = '__all__'


# ================================================= #
# ************** 问题来源 序列化器  ************** #
# ================================================= #

class QuestionOriginSerializer(CustomModelSerializer):

    class Meta:
        model = QuestionOrigin
        fields = '__all__'


class QuestionOriginUpdateSerializer(CustomModelSerializer):
    def validate(self, attrs: dict):
        return super().validate(attrs)

    class Meta:
        model = QuestionOrigin
        fields = '__all__'



