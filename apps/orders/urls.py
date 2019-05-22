# from django.contrib import admin

from django.urls import re_path, include
from rest_framework.routers import DefaultRouter

from orders.views import OrdersViewSet


router = DefaultRouter()

# 配置users的url
router.register(r'orders', OrdersViewSet, base_name="orders")


orders_urlpatterns = [
    re_path('^', include(router.urls)),
]