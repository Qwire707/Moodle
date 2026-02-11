from django.urls import path, include
from . import views

urlpatterns = [
    path('lessons_list/', views.lessons_list_view, name='lessons_list'),
    path('lesson_detail/', views.lesson_detail_view, name='lesson_detail'),
]
