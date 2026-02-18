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



def lesson_detail_view(request, pk):
    if request.method == 'GET':
        lesson = get_object_or_404(models.Lesson, pk=pk)
        module = lesson.module
        course = module.course
        # assignments = lesson.assignments.all()
        context = {}
        context['lesson'] = lesson
        context['module'] = module
        context['course'] = course
        # context['assignments'] = assignments
        return render(request,'lessons/lesson_detail.html', context)



