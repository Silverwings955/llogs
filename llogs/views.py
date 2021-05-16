# coding=UTF-8
from django.shortcuts import render
from .models import Topic


# Create your views here.
def index(request):
    """学习笔记的主页"""
    # return HttpResponse('是的，你成功了！')
    return render(request, 'llogs/index.html')


def topics(request):
    """显示所有主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics':topics}
    return render(request, 'llogs/topics.html', context)