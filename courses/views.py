from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from . import models

@login_required
def my_courses_view(request):
    pass

@login_required
def all_courses_view(request):
    if request.method == 'GET':
        context = {}
        courses = models.Courses.objects.all()
        context['courses'] = courses
        return render(request, 'courses/all_courses.html', context)

@login_required
def course_detail_view(request, pk):
    if request.method == 'GET':
        course = get_object_or_404(models.Courses, pk=pk)
        context = {}
        context['course'] = course
        return render(request, 'courses/course_detail.html', context)


@login_required
def enroll_course_view(request, course_id):
    pass

@login_required
def completed_course_view(request, course_id):
    pass

