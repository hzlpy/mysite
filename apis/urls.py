from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^hello/$', views.hello, name='hello'),
    url(r'^(?P<project_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<project_id>[0-9]+)/api/$', views.api, name='api'),
    url(r'^(?P<project_id>[0-9]+)/results/$', views.results, name='results'),
    #url(r'^layui/css/layui.css$', views.css, name='css'),
    #url(r'^layui/layui.js$', views.js, name='js'),
]
