from django.urls import path
from .views import load_json_view

urlpatterns = [
    path('load-json/', load_json_view, name='load_json_view'),
]