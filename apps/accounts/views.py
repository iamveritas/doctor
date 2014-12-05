# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from apps.accounts.forms import UserForm
from django.contrib import auth
from django.core.context_processors import csrf
from apps.accounts.models import UserProfile
from django.http import HttpResponseRedirect
from apps.internal.models import DoctorUser


def registration(request):
    args = {}
    args.update(csrf(request))
    newuser_form = UserForm()
    args['form'] = newuser_form
    args['user'] = request.user

    if request.POST:
        newuser_form = UserForm(request.POST)

        if newuser_form.is_valid():
            newuser_form.save()
#            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
#                                        password=newuser_form.cleaned_data['password1'])
#            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('accounts/registration.html', args)


def login(request):

    args = {}
    args.update(csrf(request))

    if UserProfile.objects.filter(user_id=request.user.id):
        photo = UserProfile.objects.filter(user_id=request.user.id)[0]
    else:
        photo = ''

    user = request.user
    args['photo'] = photo

    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
#            return redirect('/')
        else:
            args['login_error'] = 'Користувач не знайдений! Можливо Ви забули пароль?'

    args['user'] = user

    if DoctorUser.objects.filter(user=request.user.id):
        args['status'] = 'doctor'
    else:
        args['status'] = 'user'


    return render_to_response("accounts/login.html", args)


#    return render_to_response("accounts/login.html", {"user": request.user, "photo": photo})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login")