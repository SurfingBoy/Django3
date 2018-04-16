# -*- coding:utf-8 -*-
from django.urls import path
from .import views
from django.conf.urls import url

urlpatterns=[
    path('',views.index,name='index'),
    path('add/<int:a>/<int:b>/',views.old_add_redirect),
    url(r'new_add/(\d+)/(\d+)/$',views.add,name='add_new')
]