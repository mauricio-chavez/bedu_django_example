"""Accounts views"""

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from .forms import SignupForm


def sign_in(request):
    if request.method == 'GET':
        return render(request, 'accounts/login.html')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('accounts:profile')
        else:
            return render(request, 'accounts/login.html', {
                'message': 'Tus credenciales no existen'
            })


@login_required
def perfil(request):
    return render(request, 'accounts/perfil.html')


def signoff(request):
    logout(request)
    return redirect('accounts:login')


def signup(request):
    if request.method == 'GET':
        form = SignupForm()

    else:
        form = SignupForm(data=request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:profile')

    return render(request, 'accounts/signup.html', {'form': form})


def nombre(request, id):
    from django.http import HttpResponse
    username = User.objects.get(id=id).username
    return HttpResponse('<h1>Hola, {}</h1>'.format(username))