# coding = UTF-8
"""llogs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path

from . import views

app_name = 'llogs'
urlpatterns = [
    # 主页
    path('', views.index, name = 'index'),
    # 显示所有主题
    path('topics/', views.topics, name = 'topics'),
    path('topics/(?P<topic_id>\\d+)/', views.topic, name = 'topic'),
]
