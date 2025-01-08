from django.urls import path
from . import views
from django.urls import path, include

urlpatterns = [
    path('', views.upload_page, name='upload_page'),
    path('upload/', views.upload_file, name='upload_file'),
    path('complete/', include('complete.urls')),
]
