from django.urls import re_path
from rest_framework.routers import DefaultRouter

from . import views
from .views import QuestionsModelViewSet, QLModelViewSet, QBModelViewSet, QOModelViewSet

router = DefaultRouter()
router.register(r'question', QuestionsModelViewSet)
router.register(r'level', QLModelViewSet)
router.register(r'broad', QBModelViewSet)
router.register(r'origin', QOModelViewSet)

urlpatterns = [
    # 获取问题详情
    re_path('question/sendEmail/', QuestionsModelViewSet.as_view({'put': 'send_text'})),
]

urlpatterns += router.urls
