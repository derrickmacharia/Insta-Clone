from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from instapp import views
from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     url(r'^$',views.index,name= 'index'),

# ]

urlpatterns = [
    path('',views.index,name= 'index'),
    path('profile/', views.profile, name='profile'),
    path('upload/add/', views.save_image, name='save.image'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
