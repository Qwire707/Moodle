from django.shortcuts import render, get_object_or_404, redirect
from .models import Assignment, Submission

from lessons.models import Lesson
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .forms import SubmissionForm
from lessons.models import Lesson
from grades.models import Grade

#User
from django.conf import settings

from lessons.models import Lesson

User = settings.AUTH_USER_MODEL

def assignment_list_view(request):
    assignments = Assignment.objects.all()  # <- для /assignments/

    return render(request, 'assignments/assignment_list.html', {'assignments': assignments})

def assignment_detail_view(request, assignment_id):
    assignment = get_object_or_404(Assignment, pk=assignment_id)
    user = request.user

    if user.is_authenticated and user.role != 'student':
        return HttpResponseForbidden("Тільки студенти можуть переглядати це завдання")

    submissions = Submission.objects.filter(assignment=assignment, student=user).first()

    if request.method == 'POST':
        form = SubmissionForm(request.Post, request.FILES, instance=submissions)
        if form.is_valid():
            submissions = form.save(commit=False)
            submissions.student = user
            submissions.assignment = assignment
            submissions.save()
            return redirect('assignments:assignment_detail', assignment_id)
    else:
        form = SubmissionForm(instance=submissions)

    return render(request, 'assignments/assignment_detail.html', {'assignment': assignment,'submissions': submissions, 'form': form})


def submission_list_view(request):
    submissions = Submission.objects.filter(student=request.user)
    user = request.user

    return render(request, 'assignments/submission_list.html', {'submissions': submissions})



def grade_submission_view(request, submission_id):
    submission = get_object_or_404(Submission, pk=submission_id)
    user = request.user

    if not user.is_teacher and not user.is_staff:
        return HttpResponseForbidden("Тільки викладач або адміністратор може оцінювати")

    if request.method == 'POST':
        score = int(request.POST.get('score', 0))
        feedback = request.POST.get('feedback', '')

        from grades.models import Grade
        Grade.objects.update_or_create(
            submission=submission,
            defaults={
                'score': score,
                'feedback': feedback,
                'teacher': user,
                'max_score': submission.assignment.max_score,
            }
        )

        return redirect('submissions_list', assignments_id=submission.assignment.id)

    grade = getattr(submission, 'grade', None)

    return render(
        request,
        'assignments/grade_submission.html',
        {
            'submission': submission,
            'grade': grade
        }
    )