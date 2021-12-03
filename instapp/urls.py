from django.conf.urls import url
from django.contrib import admin
from instapp import views


urlpatterns = [
    url(r'^$',views.index,name= 'index'),

]

# urlpatterns = [
#     path('',views.index,name= 'index'),

# ]