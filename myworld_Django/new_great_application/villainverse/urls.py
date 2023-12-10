
from django.urls import path
from . import views

urlpatterns = [
    path('villainverse/', views.members, name='members'),
]