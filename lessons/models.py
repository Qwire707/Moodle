from django.db import models

from courses.models import Module
from accounts.models import CustomUser


class Lesson(models.Model):
    module = models.ForeignKey(Module, on_delete=models.CASCADE, verbose_name='lessons')
    title = models.CharField(max_length=100)
    content = models.ImageField()
    image = models.ImageField(upload_to='lessons/images/', blank=True, null=True, verbose_name='image')
    video_url = models.URLField(blank=True, null=True, verbose_name='video url')
    order = models.PositiveIntegerField(default=0, verbose_name='order')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='created at')

    class Meta:
        ordering = ['order']
        unique_together = ('module', 'order')
        verbose_name_plural = 'уроки'
        verbose_name = "урок"

    def __str__(self):
        return f"{self.module.title} - {self.title}"

