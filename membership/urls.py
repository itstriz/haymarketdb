from django.conf.urls import patterns, url

from membership import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
