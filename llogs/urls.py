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
from django.urls import path, re_path

from . import views

app_name = 'llogs'
urlpatterns = [
    # 主页
    path('', views.index, name = 'index'),
    # 显示所有主题
    path('topics/', views.topics, name = 'topics'),

    # (?P<topic_id>\d+)捕获一个数字值，并将其存储在变量topic_id中
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = 'topic'),

    re_path(r'^new_topic/$', views.new_topic, name = 'new_topic'),
    re_path(r'^new_entry/(?P<topic_id>\d+)/$', views.new_entry,
            name = 'new_entry'),
    re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry,
            name = 'edit_entry')
]
