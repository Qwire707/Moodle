from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    STUDENT = 'student'
    TEACHER = 'teacher'
    ADMIN = 'admin'

    ROLE_CHOICES = [
        (STUDENT, 'Student'),
        (TEACHER, 'Teacher'),
        (ADMIN, 'Admin'),
    ]

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default=STUDENT
    )
    date_of_birth = models.DateField(null=True, blank=True, verbose_name="Дата народження")
    avatar = models.ImageField(upload_to='avatars/', null=True, blank=True, verbose_name="Аватар")
    bio = models.TextField(blank=True, verbose_name="Про себе")
    phone = models.CharField(max_length=20, blank=True, verbose_name="Телефон")
    class Meta:
        verbose_name = "Користувач"
        verbose_name_plural = "Користувачі"

    def __str__(self):
        return self.username
