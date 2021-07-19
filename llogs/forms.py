# coding=UTF-8
from django import forms
from .models import Topic, Entry


# 添加新主题
class TopicForm(forms.ModelForm):
    class Meta:
        # 根据模型Topic创建一个新表单
        model = Topic
        # 表单只包含字段text
        fields = ['text']
        # 不为字段text生成标签
        labels = {'text': ''}


# 添加新条目
class EntryForm(forms.ModelForm):
    class Meta:
        # 根据模型Entry创建一个新表单
        model = Entry
        # 表单包含一个字段text
        fields = ['text']
        # 不生成字段标签
        labels = {'text': ''}

        '''定义属性widgets(一个HTML表单元素:单行文本框、多行文本区域或下拉列表),设置该属性，
        可以覆盖Django选择的默认小部件。此处我们定制了字段text的输入小部件，将文本部件
        设置为80列而不是默认的40列'''
        widgets = {'text': forms.Textarea(attrs = {'cols': 80})}
