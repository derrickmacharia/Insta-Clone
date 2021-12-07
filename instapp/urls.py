from django.conf.urls import url
from django.contrib import admin
from django.urls import path,re_path
from . import views as main_views
from instapp import views



# urlpatterns = [
#     url(r'^$',views.index,name= 'index'),

# ]

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('like/', views.like_image, name='like-image'),
    path('search/', views.search_post, name='search.post'),
    # path('image/<int:id>/', views.single_pic, name='single.pic'),
    path('user/<user_id>/', views.user_profile, name='user.profile'),
    path('comments/<image_id>', views.comments,name='comments'),
]

