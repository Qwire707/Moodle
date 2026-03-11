from django.urls import path, include
from . import views

urlpatterns = [
    path('lesson_list/', views.lessons_list_view, name='lessons-list'),
    path('<int:pk>', views.lesson_detail_view, name='lesson-detail'),
    path('lessons/<int:pk>/delete-file/', views.lesson_delete_file, name='lesson-delete-file'),
]
