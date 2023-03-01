from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.shortcuts import render, redirect
from app_users.forms import AuthForm


def login_view(request):
    if request.method == 'POST':  # for POST requests try auth user
        auth_form = AuthForm(request.POST)
        if auth_form.is_valid():
            username = auth_form.cleaned_data['username']
            password = auth_form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user:
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    auth_form.add_error('__all__', 'Ошибка: учетная запись не активна.')
            else:
                auth_form.add_error('__all__', 'Ошибка: проверьте правильность написания логина и пароля.')
    else:  # for other requests just show login page
        auth_form = AuthForm()
    context = {
        'form': auth_form
    }
    return render(request, 'users/login.html', context=context)


def logout_view(request):
    logout(request)
    return redirect('home')