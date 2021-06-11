# coding=UTF-8
from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """学习笔记的主页"""
    # return HttpResponse('是的，你成功了！')
    return render(request, 'llogs/index.html')


# 从服务器收到对象request
def topics(request):
    """显示所有主题"""
    # 查询数据库，提供Topic对象，并按照属性date_added进行排序，将返回的查询集存储在topics中
    topics = Topic.objects.order_by('date_added')
    # 将上下文存储于字典，键是主题，值是发送内容
    context = {'topics': topics}
    # 将对象request和模版路径还有context传递给render
    return render(request, 'llogs/topics.html', context)


# 捕获表达式的值，存储到topic_id中
def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    # 使用get()来获取指定的主题
    topic = Topic.objects.get(id = topic_id)
    # 获取与该主题相关联的条目并将它们按照date_added排序,减号指定按照降序排列使最近条目先显示
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entrise': entries}
    return render(request, 'llogs/topics.html', context)