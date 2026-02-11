from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.my_courses_view, name='my_courses'),
    path('all/', views.all_courses_view, name='all_courses'),
    path('course/', views.course_detail_view, name='course_detail'),
    path('enroll/<int:pk>', views.enroll_course_view, name='enroll_course'),
    path('completed/', views.completed_course_view, name='completed_course'),
]