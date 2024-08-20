from django.urls import path
from . import views

urlpatterns = [
    path('', views.inspection_list, name='inspection_list'),
    path('create/', views.inspection_create, name='inspection_create'),
    path('<int:id>/edit/', views.inspection_update, name='inspection_update'),
    path('<int:id>/delete/', views.inspection_delete, name='inspection_delete'),
    path('<int:id>/', views.inspection_detail, name='inspection_detail'),  # Detail view URL
]
