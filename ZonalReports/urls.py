from django.urls import path
from . import views

urlpatterns = [
    path('zonal_report/new/', views.zonal_report_create, name='zonal_report_create'),
    path('zonal_reports/', views.zonal_report_list, name='zonal_report_list'),
    path('zonal_report/<int:pk>/', views.zonal_report_detail, name='zonal_report_detail'),
    path('zonal_reports/filter/', views.zonal_report_filter, name='zonal_report_filter'),
    path('zonal_report/<int:pk>/pdf/', views.generate_pdf, name='generate_pdf'),
    path('zonal_report/<int:pk>/excel/', views.generate_excel, name='generate_excel'),
    path('zonal_report/<int:pk>/bar_graph/', views.generate_bar_graph, name='generate_bar_graph'),
    path('zonal_report/<int:pk>/edit/', views.zonal_report_update, name='zonal_report_update'),
    path('zonal_report/<int:pk>/delete/', views.zonal_report_delete, name='zonal_report_delete'),
]
