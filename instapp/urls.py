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
    path('like/', views.like_image, name='like-image'),
    path('search/', views.search_post, name='search.post'),
    
]

