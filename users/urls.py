from django.contrib import admin
from django.urls import path,re_path
from users import views

app_name = 'users'
urlpatterns = [
    #path("", views.index,name="index"),
    re_path(r'^(?P<pk>[0-9]+)/$',views.userprofile,name="profile"),
]