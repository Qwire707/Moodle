from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.models import Courses
from . import models


def lessons_list_view(request):
    if request.method == 'GET':
        lesson = models.Lesson.objects.all()
        context = {}
        context['lessons'] = lesson
        return render(request,'lessons/lesson_list.html', context)



from django.shortcuts import render, get_object_or_404, redirect
from . import models

from django.shortcuts import render, get_object_or_404, redirect
from .models import Lesson

def lesson_detail_view(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    module = lesson.module
    course = module.course

    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')  # отримуємо файл з форми

        if uploaded_file:
            lesson.content = uploaded_file  # зберігаємо файл
            lesson.save()  # обовʼязково save

        return redirect('lesson-detail', pk=lesson.pk)  # оновлюємо сторінку

    context = {
        'lesson': lesson,
        'module': module,
        'course': course,
    }
    return render(request, 'lessons/lesson_detail.html', context)

def lesson_delete_file(request, pk):
    lesson = get_object_or_404(Lesson, pk=pk)

    if request.method == "POST":
        lesson.content.delete(save=True)
    return redirect('lesson-detail', pk=lesson.pk)



