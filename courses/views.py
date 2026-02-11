from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

@login_required
def my_courses_view(request):
    pass

@login_required
def all_courses_view(request):
    pass

@login_required
def course_detail_view(request, course_id):
    pass

@login_required
def enroll_course_view(request, course_id):
    pass

@login_required
def completed_course_view(request, course_id):
    pass

