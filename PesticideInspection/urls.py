from django.urls import path
from . import views

urlpatterns = [
    path('', views.pesticide_inspection_list, name='pesticide_inspection_list'),
    path('pesticide-inspections/<int:id>/', views.pesticide_inspection_detail, name='pesticide_inspection_detail'),
    path('pesticide-inspections/new/', views.pesticide_inspection_create, name='pesticide_inspection_create'),
    path('pesticide-inspections/<int:id>/edit/', views.pesticide_inspection_update, name='pesticide_inspection_update'),
    path('pesticide-inspections/<int:id>/delete/', views.pesticide_inspection_delete, name='pesticide_inspection_delete'),
]
