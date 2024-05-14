# myproject/urls.py
from django.urls import path
from .views import event_list

urlpatterns = [
    path('events/', event_list),
]