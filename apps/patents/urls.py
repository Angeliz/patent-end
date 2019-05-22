# from django.contrib import admin

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from patents.views import PatentsViewSet


router = DefaultRouter()

# 配置users的url
router.register(r'patents', PatentsViewSet, base_name="patents")


patents_urlpatterns = [
    re_path('^', include(router.urls)),
]