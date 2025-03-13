from django.shortcuts import render
from rest_framework import generics
from .models import Course
from .serializers import CourseSerializer

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
from users.models import User

class CourseListCreateView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class AddRemoveStudentView(APIView):
    def post(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        student = get_object_or_404(User, pk=request.data.get('student_id'), role='Student')
        course.students.add(student)
        return Response({'message': 'Student added'}, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        course = get_object_or_404(Course, pk=pk)
        student = get_object_or_404(User, pk=request.data.get('student_id'), role='Student')
        course.students.remove(student)
        return Response({'message': 'Student removed'}, status=status.HTTP_200_OK)
