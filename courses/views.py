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

from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def course_list(request):
    courses = Course.objects.all()
    serializer = CourseSerializer(courses, many=True)
    return Response(serializer.data)

from rest_framework.decorators import api_view, permission_classes
from .permissions import IsManager

@api_view(['POST'])
@permission_classes([IsManager])
def add_course(request):
    serializer = CourseSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=201)
    return Response(serializer.errors, status=400)
