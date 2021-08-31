from django.urls import re_path
from rest_framework.routers import DefaultRouter

from .views import QuesFollowModelViewSet, DailyProgressModelViewSet

router = DefaultRouter()
router.register(r'questionFollow', QuesFollowModelViewSet)
router.register(r'DailyProgress', DailyProgressModelViewSet)

urlpatterns = [
    re_path('questionFollow/sendFollowEmail/', QuesFollowModelViewSet.as_view({'put': 'send_follow_email'})),
    re_path('questionFollow/resetStatus/', QuesFollowModelViewSet.as_view({'put': 'reset_status'}))
]

urlpatterns += router.urls
