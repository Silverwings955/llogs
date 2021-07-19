# coding=UTF-8
from django.shortcuts import render
from .models import Topic, Entry
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import TopicForm, EntryForm


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
    topic = Topic.objects.get(id=topic_id)
    # 获取与该主题相关联的条目并将它们按照date_added排序,减号指定按照降序排列使最近条目先显示
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'llogs/topic.html', context)


# 显示一个空表单，对提交的表单数据惊醒处理，并将用户重定向到网页topics.
def new_topic(request):
    """添加新主题"""
    if request.method != 'POST':
        # 未提交数据: 创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('llogs:topics'))
    context = {'form': form}
    return render(request, 'llogs/new_topic.html', context)


def new_entry(request, topic_id):
    """在特定主题中添加新条目"""
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()

    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data = request.POST)
        if form.is_valid():
            new_entry = form.save(commit = False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('llogs:topic',
                                                args = [topic_id]))
    context = {'topic': topic, 'form': form}
    return render(request, 'llogs/new_entry.html', context)


def edit_entry(request, entry_id):
    """编辑既有条目"""
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method !='POST':
        # 初次请求，使用当前条目填充表单
        form = EntryForm(instance = entry)
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(instance = entry, data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('llogs:topic',
                                                args = [topic.id]))

    context = {'entry': entry, 'topic':topic, 'form':form}
    return render(request, 'llogs/edit_entry.html', context)