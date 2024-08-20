# reporting/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.meeting_report_list, name='meeting_report_list'),
    path('create/', views.meeting_report_create, name='meeting_report_create'),
    path('<int:pk>/', views.meeting_report_detail, name='meeting_report_detail'),
    path('meeting_report/<int:pk>/update/', views.update_meeting_report, name='update_meeting_report'),
    path('meeting_report/<int:pk>/delete/', views.delete_meeting_report, name='delete_meeting_report'),
]
