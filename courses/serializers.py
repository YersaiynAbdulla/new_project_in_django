from rest_framework import serializers
from .models import Course
from users.models import User

class CourseSerializer(serializers.ModelSerializer):
    students = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='Student'), many=True)
    teacher = serializers.PrimaryKeyRelatedField(queryset=User.objects.filter(role='Manager'))

    class Meta:
        model = Course
        fields = '__all__'