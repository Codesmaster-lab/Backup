
#home URL Configuration
from django.urls import path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from . import views
from .views import profile_view
urlpatterns = [
    path('SignIn/',auth_views.LoginView.as_view(template_name='Users/signin.html'),name='Codesmaster_SignIn'),
    path('SignUp/',views.signup,name='Codesmaster_SignUp'),
    path('Signout/',auth_views.LogoutView.as_view(template_name='Users/signout.html'),name='Codesmaster_SignOut'),
    path('Profile/',views.profile,name='Codesmaster_Profile'),
    path('user/<int:pk>/',profile_view.as_view(),name='Codesmaster_ProfileView')

]
if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
