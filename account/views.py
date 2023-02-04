from django.shortcuts import render, redirect
from .forms import RegisterForm, LoginForm, authenticate
from django.contrib import messages
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User


def user_login(request):
    if request.user.is_authenticated:
        return redirect('home:main')
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # user = User.objects.get(username=form.cleaned_data.get('username'))
            user = authenticate(username=form.cleaned_data.get('username'), password=form.cleaned_data.get('password'))
            login(request, user)
            messages.success(request, 'لاگین با موفقیت انجام شد', extra_tags='success')
            return redirect('home:main')
        else:
            messages.error(request, form.non_field_errors(), extra_tags='danger')

    else:
        form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def user_register(request):
    if request.user.is_authenticated:
        return redirect('home:main')

    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            email = form.cleaned_data.get('email')
            print(username, password, email, type(password))
            User.objects.create_user(username=username, email=email, password=password)
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, 'ثبت نام با موفقیت انجام شد', extra_tags='success')
            return redirect('home:main')
        else:
            for e in form.errors.values():
                messages.error(request, e, extra_tags='danger')
    else:
        form = RegisterForm()
    return render(request, 'account/register.html', {'form': form})


@login_required
def user_logout(request):
    logout(request)
    return redirect('account:login')


@login_required
def user_profile(request, user_id):
    user = User.objects.get(id=user_id)
    if request.user == user:
        return render(request, 'account/profile.html', {'user': user})
    else:
        return redirect('home:main')
