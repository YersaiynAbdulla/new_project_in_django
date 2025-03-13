from django.urls import path
from .views import CourseListCreateView, CourseDetailView, AddRemoveStudentView

urlpatterns = [
    path('courses/', CourseListCreateView.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseDetailView.as_view(), name='course-detail'),
    path('courses/<int:pk>/students/', AddRemoveStudentView.as_view(), name='course-add-remove-student'),
]
