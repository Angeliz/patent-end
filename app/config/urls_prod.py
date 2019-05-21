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
from django.urls import path
from rest_framework_jwt.views import obtain_jwt_token

from users.urls import users_urlpatterns
# from todo.urls import todo_urlpatterns
# from apps.projects import projects_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    # 通过用户名密码获取 JWT
    path('users/obtain_token', obtain_jwt_token)
    # 通过未过期 JWT 来刷新 JWT。
    # path('auth/refresh_token/', refresh_jwt_token),

]

urlpatterns = users_urlpatterns + todo_urlpatterns + projects_urlpatterns + urlpatterns
