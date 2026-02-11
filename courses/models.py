from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Courses(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ManyToManyField(
        User,
        verbose_name='courses'
    )
    student = models.ManyToManyField(User,related_name='student_courses')
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Курс'
        verbose_name_plural = 'Курси'

class Module(models.Model):
    course = models.ForeignKey(Courses,
    on_delete=models.CASCADE,
    related_name='modules'
    )
    title = models.CharField(max_length=255)
    order = models.PositiveIntegerField()

    class Meta:
        ordering = ['order']
        unique_together = ('course', 'order')
        verbose_name = 'Mодуль'
        verbose_name_plural = 'Mодулі'

    def __str__(self):
        return self.title
