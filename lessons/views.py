from rest_framework import generics
from .models import Lesson
from .serializers import LessonSerializer
from courses.models import Course

class CourseLessonsList(generics.ListAPIView):
    serializer_class = LessonSerializer

    def get_queryset(self):
        course_id = self.kwargs['course_id']
        return Lesson.objects.filter(course_id=course_id)

class LessonDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer

class LessonCreate(generics.CreateAPIView):
    queryset = Lesson.objects.all()
    serializer_class = LessonSerializer
