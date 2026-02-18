from django.urls import path
from . import views

urlpatterns = [
    path('my/', views.my_courses_view, name='my-courses'),
    path('all/', views.all_courses_view, name='all-courses'),
    path('<int:pk>', views.course_detail_view, name='course-detail'),
    path('enroll/<int:pk>', views.enroll_course_view, name='enroll-course'),
    path('completed/', views.completed_course_view, name='completed-course'),
]