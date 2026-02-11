from django.db import models
from django.conf import settings

from lessons.models import Lesson

User = settings.AUTH_USER_MODEL

class Assignment(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=models.CASCADE, verbose_name='assignment')
    title = models.CharField(verbose_name='title', max_length=100)
    description = models.TextField(verbose_name='description')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='updated at')

    def __str__(self):
        return f"{self.lesson.title} - {self.title}"

    class Meta:
        unique_together = ('lesson', 'title')
        ordering = ['-created_at']
        verbose_name_plural = "Всі завдання"
        verbose_name = "Завдання"

class Submission(models.Model):
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='submissions')
    student = models.ForeignKey(User, on_delete=models.CASCADE, related_name='students_submissions')
    file = models.FileField(upload_to='submissions/',verbose_name='Файл роботи')
    comment = models.TextField(blank=True,null=True,verbose_name='Коментар студента')
    deadline = models.DateField(verbose_name="Дедлайн")
    submitted_at = models.DateTimeField(auto_now_add=True,verbose_name='Дата здачі')
    updated_at = models.DateTimeField(auto_now=True,verbose_name='Дата оновлення')


    class Meta:
        unique_together = ('assignment', 'student')
        ordering = ['-submitted_at']
        verbose_name = 'Завдання на виконання'

    def __str__(self):
        return f'{self.student.first_name} → {self.assignment.title}'

    class Meta:
        unique_together = ('assignment', 'student')
        ordering = ['-submitted_at']
        verbose_name = "Завдання до виконання"