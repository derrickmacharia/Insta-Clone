from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from instapp import views


# urlpatterns = [
#     url(r'^$',views.index,name= 'index'),

# ]

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),


]