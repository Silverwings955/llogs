# coding=UTF-8
from django.shortcuts import render


# Create your views here.
def index(request):
    """学习笔记的主页"""
    # return HttpResponse('是的，你成功了！')
    return render(request, 'llogs/index.html')
