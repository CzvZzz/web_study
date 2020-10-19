'''定义learnin_logs的URl模式'''

from django.urls import path, re_path

from . import views

urlpatterns = [
    # 主页
    path('', views.index, name='index'),

    path('Pizza_index', views.Pizza_index, name='Pizza_index'),

    # 显示所有的主题
    path('topics/', views.topics, name='topics'),

    path('Pizza_names/', views.Pizza_names, name='Pizza_names'),

    # 特定主题的详细页面
    re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name='topic'),

    re_path(r'^Pizza_names/(?P<name_id>\d+)/$', views.Pizza_name, name='Pizza_name'),

    # 用于添加新主题的网页
    path('new_topic/', views.new_topic, name='new_topic'),

    # 用于添加新条目的页面
    re_path(r'new_entry/(?P<topic_id>\d+)/$', views.new_entry, name='new_entry'),

    # 用于编辑条目的页面
    re_path(r'edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name='edit_entry'),

    ]