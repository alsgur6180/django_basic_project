from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm


def home(request):
    user_id = request.session.get('user')

    if user_id:
        user = UserInfo.objects.get(pk=user_id)
        return HttpResponse(user.username)
    return HttpResponse('Home!')


def logout(request):
    if request.session.get('user'):
        del(request.session['user'])
    return redirect('/')


def login(request):
    form = LoginForm()
    return render(request, 'login.html', {'form': form})


def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    elif request.method == 'POST':
        username = request.POST.get('username', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        re_password = request.POST.get('re-password', None)

        res_data = {}
        if not (username and password and re_password and email):
            res_data['error'] = '모든 값을 입력해야 합니다.'

        elif password != re_password:
            res_data['error'] = '비밀번호가 다릅니다.'
        else:

            user = UserInfo(
                username=username,
                email=email,
                password=make_password(password)
            )

            user.save()
        return render(request, 'register.html', res_data)