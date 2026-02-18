from django.urls import path, include
from . import views

urlpatterns = [
    path('lesson_list/', views.lessons_list_view, name='lessons-list'),
    path('<int:pk>', views.lesson_detail_view, name='lesson-detail'),
]
