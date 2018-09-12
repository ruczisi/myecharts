from django.contrib import admin
from django.urls import path,re_path
from hele import views

urlpatterns = [
    path("", views.index,name="index"),
    re_path("^town/(?P<pk>[0-9]+)/$",views.get_school,name="get_school"),
    re_path("^school/(?P<pk>[0-9]+)/$",views.myechart,name="myechart"),
    path("all/",views.all_school,name="all_school"),
]