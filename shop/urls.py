# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    # url(r'^stores/$', views.store_list, name='store_list'),
    url(r'^stores/$', views.StoreListView.as_view(), name='store_list')
]