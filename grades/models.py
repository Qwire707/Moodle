from django.db import models

from accounts.models import CustomUser
from assignments.models import Submission


class Grade(models.Model):
    submission = models.OneToOneField(Submission, on_delete=models.CASCADE, verbose_name="grade")

    teacher = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True,
        blank=True, verbose_name="given_grades")

    score = models.PositiveIntegerField(default=0)
    max_score = models.PositiveIntegerField(default=12)

    feedback = models.TextField(blank=True)

    graded_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-graded_at']

    def __str__(self):
        return f"{self.score}/{self.max_score}"