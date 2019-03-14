from django.contrib import admin
from django.urls import path
from . import views

app_name = "boards"


urlpatterns = [
    path('<int:pk>/edit/', views.edit, name = 'edit'),
    path('<int:pk>/delete/', views.delete, name = 'delete'),
    path('<int:pk>/detail/', views.detail, name = 'detail'),
    path('new/', views.new, name = 'new'),
    path('', views.index, name ='index'),
]
    