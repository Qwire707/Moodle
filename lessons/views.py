from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.models import Courses
from .models import Lesson

def lessons_list_view(request, course_id):
    course = get_object_or_404(Courses, pk=course_id, is_published=True)

    lessons = Lesson.objects.filter(course=course)

    return render(request,
                  'lessons/lesson_list.html',
                  {
                      'course': course,
                      'lessons': lessons
                  }
    )

def lesson_detail_view(request, course_id, lesson_id):
    course = get_object_or_404(Courses, pk=course_id, is_published=True)

    lesson = get_object_or_404(Lesson, pk=lesson_id, course=course)

    assignments = lesson.assignments.all()

    return render(request,
                  'lessons/lesson_detail.html',
                  {
                      'course': course,
                      'lesson': lesson,
                      'assignments': assignments
                  }
    )



