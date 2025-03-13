from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.core.paginator import Paginator
from .models import User
from .forms import UserRegisterForm
import random

verification_codes = {} 

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            code = random.randint(100000, 999999)
            verification_codes[user.email] = code
            send_mail(
                'Код подтверждения',
                f'Ваш код: {code}',
                'noreply@outpeer.com',
                [user.email],
                fail_silently=False,
            )
            request.session['user_data'] = form.cleaned_data
            return redirect('verify')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})

def verify_code(request):
    if request.method == "POST":
        email = request.session.get('user_data', {}).get('email')
        entered_code = request.POST.get('code')
        if email in verification_codes and verification_codes[email] == int(entered_code):
            user_data = request.session.pop('user_data')
            User.objects.create_user(**user_data)
            return redirect('login')
    return render(request, 'users/verify.html')

def user_list(request):
    users = User.objects.all()
    paginator = Paginator(users, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'users/user_list.html', {'page_obj': page_obj})
