from django.urls import path
from .views import CourseLessonsList, LessonDetail, LessonCreate

urlpatterns = [
    path('course/<int:course_id>/lessons/', CourseLessonsList.as_view(), name='course-lessons'),
    path('lesson/<int:pk>/', LessonDetail.as_view(), name='lesson-detail'),
    path('lesson/create/', LessonCreate.as_view(), name='lesson-create'),
]
