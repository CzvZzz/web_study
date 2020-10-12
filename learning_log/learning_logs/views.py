from django.shortcuts import render

from .models import Topic, Pizza

from django.http import HttpResponseRedirect

from django.urls import reverse

from .forms import TopicForm, EntryForm

# Create your views here.

def index(request):
    """学习笔记的主页"""
    return render(request, 'learning_logs/index.html')

def Pizza_index(request):
    """披萨的主页"""
    return render(request, 'learning_logs/Pizza_index.html')

def topics(request):
    """显示所有的主题"""
    topics = Topic.objects.order_by('date_added')
    context = {'topics': topics}
    return render(request, 'learning_logs/topics.html', context)

def Pizza_names(request):
    '''显示所有的披萨的名称'''
    names = Pizza.objects.order_by('date_added')
    context = {'Pizza_names': names}
    return render(request, 'learning_logs/Pizza_names.html', context)

def topic(request, topic_id):
    """显示单个主题及其所有的条目"""
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry_set.order_by('-date_added')
    context = {'topic': topic, 'entries': entries}
    return render(request, 'learning_logs/topic.html', context)

def Pizza_name(request, name_id):
    """显示披萨及其所有的配料"""
    name = Pizza.objects.get(id=name_id)
    toppings = name.topping_set.order_by('-date_added')
    context = {'name': name, 'toppings': toppings}
    return render(request, 'learning_logs/Pizza_name.html', context)

def new_topic(request):
    '''添加新主题'''
    if request.method != 'POST':
        # 未提交数据：创建一个新表单
        form = TopicForm()
    else:
        # POST提交的数据，对数据进行处理
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('learning_logs:topics'))

    context = {'form': form}
    return render(request, 'learning_logs/new_topic.html', context)

def new_entry(request, topic_id):
    '''在特定的主题中添加新条目'''
    topic = Topic.objects.get(id=topic_id)

    if request.method != 'POST':
        # 未提交数据，创建一个空表单
        form = EntryForm()
    else:
        # POST提交的数据，对数据进行处理
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return HttpResponseRedirect(reverse('learning_logs:topic', args=[topic_id]))

    context = {'topic': topic, 'form': form}
    return render(request, 'learning_logs/new_entry.html', context)