from django.urls import path
from . import views # . means the current folder

urlpatterns = [
    path("", views.index),
    path('new', views.new)
]
