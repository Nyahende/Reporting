from django.urls import path
from . import views

urlpatterns = [
    path('training/new/', views.training_create, name='training_create'),
    path('training/<int:pk>/edit/', views.training_update, name='training_update'),
    path('training/<int:pk>/delete/', views.training_delete, name='training_delete'),
    path('', views.training_list, name='training_list'),
    path('training/<int:pk>/', views.training_detail, name='training_detail'),
]

