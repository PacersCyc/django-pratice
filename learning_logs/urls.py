from django.urls import include, path, re_path

from . import views

urlpatterns = [
  # 主页
  re_path(r'^$', views.index, name = "index"),
  # 显示所有主题
  re_path(r'^topics/$', views.topics, name = "topics"),
  # 特定主题的详细页面
  re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = "topic"),
  # 添加主题页
  re_path(r'^new_topic/$', views.new_topic, name = "new_topic"),
  # 添加条目页
  re_path(r'^new_entry/(?P<topic_id>\d+)$', views.new_entry, name = "new_entry"),
  # 编辑条目页
  re_path(r'^edit_entry/(?P<entry_id>\d+)/$', views.edit_entry, name = "edit_entry"),
]
