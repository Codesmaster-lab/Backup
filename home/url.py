
#home URL Configuration
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from . import views

urlpatterns = [
    path('',views.home,name='Home'),
    path('team',views.team,name='Team'),
]

if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
