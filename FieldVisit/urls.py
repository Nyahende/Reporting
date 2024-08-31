

from django.urls import path
from . import views

urlpatterns = [
    path('', views.field_visit_report_list, name='field_visit_report_list'),
    path('create/', views.field_visit_report_create, name='field_visit_report_create'),
    path('<int:pk>/', views.field_visit_report_detail, name='field_visit_report_detail'),
    path('fieldvisits/field_visit/<int:pk>/update/', views.update_field_visit, name='update_field_visit'),
    path('field_visit/<int:pk>/delete/', views.delete_field_visit, name='delete_field_visit'),
]
