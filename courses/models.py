from django.db import models
from users.models import User

class Course(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    students = models.ManyToManyField(User, related_name='courses', limit_choices_to={'role': 'Student'})
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, related_name='teaching_courses', limit_choices_to={'role': 'Manager'})

    def __str__(self):
        return self.name