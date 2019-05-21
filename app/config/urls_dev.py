"""end URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions
from rest_framework_jwt.views import obtain_jwt_token

from users.urls import users_urlpatterns
# from todo.urls import todo_urlpatterns
# from apps.projects import projects_urlpatterns

schema_view = get_schema_view(
    openapi.Info(
        title='miaomiaomiao  API',
        default_version='v1',
        description='2333'
        # terms_of_service="https://www.google.com/policies/terms/",
        # contact=openapi.Contact(email="zhangbaiju@memect.co"),
        # license=openapi.License(name="BSD License"),
    ),
    # validators=['flex', 'ssv'],

    # https://github.com/axnsan12/drf-yasg#a-get-schema-view-parameters
    # API base url;
    # url='http://192.168.0.175:9876',
    public=True,
    permission_classes=(permissions.AllowAny,)
)

# 自动生成文档 swagger
url_docs_patterns = [
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=None), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=None), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=None), name='schema-redoc')
]

urlpatterns = [
    path('admin/', admin.site.urls),
    # 通过用户名密码获取 JWT
    path('users/obtain_token', obtain_jwt_token)
    # 通过未过期 JWT 来刷新 JWT。
    # path('auth/refresh_token/', refresh_jwt_token),

]

urlpatterns = url_docs_patterns + users_urlpatterns + urlpatterns
# urlpatterns = url_docs_patterns + users_urlpatterns + todo_urlpatterns + projects_urlpatterns + urlpatterns
