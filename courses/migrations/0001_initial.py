# Generated by Django 5.1.6 on 2025-03-13 09:51

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('students', models.ManyToManyField(limit_choices_to={'role': 'Student'}, related_name='courses', to=settings.AUTH_USER_MODEL)),
                ('teacher', models.ForeignKey(limit_choices_to={'role': 'Manager'}, on_delete=django.db.models.deletion.CASCADE, related_name='teaching_courses', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
