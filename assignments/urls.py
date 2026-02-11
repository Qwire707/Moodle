from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.assignment_list_view, name='assignment_list'),
    path('detail/<int:pk>', views.assignment_detail_view, name='assignment_detail'),
    path('submission_list', views.submission_list_view, name='submission_list'),
    path('grade_submission/<int:pk>', views.grade_submission_view, name='grade_submission')
]