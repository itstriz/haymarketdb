from django.conf.urls import patterns, url

from membership import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^shops/(?P<shop_id>\d+)/$', views.shop_detail, name='shop_detail'),
)
