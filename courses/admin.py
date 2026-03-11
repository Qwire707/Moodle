from django.contrib import admin
from courses.models import Courses, Module, EnrolledCourses

admin.site.register(Courses)
admin.site.register(Module)
admin.site.register(EnrolledCourses)