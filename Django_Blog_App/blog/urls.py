from django.urls import path
from . import views

urlpatterns = [
    path('', views.Post_list, name='Post_list'),
    path('post_detail/<int:pk>/', views.post_detail_page, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('register/', views.register_user, name='regsiter'),


]
