from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import PostDetailView,PostListView,PostCreateView,PostUpdateView,PostDeleteView
from . import views

urlpatterns = [
    path('Projects/',PostListView.as_view(),name='Codesmaster_Projects'),
    path('Projects/<int:pk>/',PostDetailView.as_view(),name='Codesmaster_Projects_Read'),
    path('Projects/create/', PostCreateView.as_view(), name='Codesmaster_Projects_Create'),
    path('Projects/<int:pk>/update/', PostUpdateView.as_view(), name='Codesmaster_Projects_Update'),
    path('Projects/<int:pk>/delete/', PostDeleteView.as_view(), name='Codesmaster_Projects_Delete')

]

if settings.DEBUG:
     urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)