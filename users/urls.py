from django.urls import path
from .views import register, verify_code, user_list
from django.shortcuts import redirect

def redirect_to_list(request):
    return redirect('user_list')

urlpatterns = [
    path('', redirect_to_list),
    path('register/', register, name='register'),
    path('verify/', verify_code, name='verify'),
    path('list/', user_list, name='user_list'),  # Оставляем только один URL для списка
]
