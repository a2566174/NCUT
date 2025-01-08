from django.urls import path
from . import views

urlpatterns = [
    path('', views.display_data, name='display_data'),
    path('remove_item/<str:order_id>/', views.remove_item, name='remove_item'),
    path('refresh/', views.refresh_data, name='refresh_data'),
]