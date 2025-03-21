
from django.db import models
from courses.models import Course

class Lesson(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    additional_material = models.URLField(blank=True, null=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="lessons")

    def __str__(self):
        return self.title