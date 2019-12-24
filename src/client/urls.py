from django.urls import path

from . import views

urlpatterns = [
    path(r'', views.login),
    path('register/', views.register),
    path('details/', views.details),
]
