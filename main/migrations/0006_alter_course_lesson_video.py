# Generated by Django 4.1.7 on 2023-03-20 06:44

import cloudinary.models
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_course_lesson_title_course_lesson_video'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='lesson_video',
            field=cloudinary.models.CloudinaryField(max_length=255, null=True, verbose_name='lesson_video'),
        ),
    ]
