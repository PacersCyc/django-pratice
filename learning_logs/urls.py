from django.urls import include, path, re_path

from . import views

urlpatterns = [
  # 主页
  re_path(r'^$', views.index, name = "index"),
  # 显示所有主题
  re_path(r'^topics/$', views.topics, name = "topics"),
  # 特定主题的详细页面
  re_path(r'^topics/(?P<topic_id>\d+)/$', views.topic, name = "topic")
]
