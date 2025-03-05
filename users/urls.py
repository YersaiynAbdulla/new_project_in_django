from django.urls import path
from .views import register, verify_code, user_list

urlpatterns = [
    path('register/', register, name='register'),
    path('verify/', verify_code, name='verify'),
    path('users/', user_list, name='user_list'),
    path('list/', user_list, name='user-list'),
]
