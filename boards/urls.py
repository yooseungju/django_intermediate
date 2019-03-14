from django.contrib import admin
from django.urls import path
from . import views

app_name = "boards"


urlpatterns = [   
    path('<int:board_pk>/comments/<int:comment_pk>/delete/', views.comments_delete, name = 'comments_delete'),
    path('<int:board_pk>/comments/', views.comments_create, name = 'comments_create'),
    path('<int:board_pk>/edit/', views.edit, name = 'edit'),
    path('<int:board_pk>/delete/', views.delete, name = 'delete'),
    path('<int:board_pk>/detail/', views.detail, name = 'detail'),
    path('new/', views.new, name = 'new'),
    path('', views.index, name ='index'),
]
    