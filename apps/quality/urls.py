from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import QuestionsModelViewSet, QLModelViewSet, QBModelViewSet, QOModelViewSet

router = DefaultRouter()
router.register(r'question', QuestionsModelViewSet)
router.register(r'level', QLModelViewSet)
router.register(r'broad', QBModelViewSet)
router.register(r'origin', QOModelViewSet)

urlpatterns = [
]

urlpatterns += router.urls