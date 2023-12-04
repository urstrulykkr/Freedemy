from django.contrib import admin

# Register your models here.

from .models import Library, Course, Enrollment

admin.site.register(Library)
admin.site.register(Course)
admin.site.register(Enrollment)