# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from apps.accounts.forms import UserForm, LoginForm
from django.contrib import auth
from django.core.context_processors import csrf
from apps.accounts.models import UserProfile
from django.http import HttpResponseRedirect
from apps.internal.models import DoctorUser, Comment

from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse


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


class LoginForm(FormView):

    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = '/doctors/'

    def __init__(self):
        self.form_errors = '1'
    '''
    def post(self, form):
        self.username = form.username
        self.password = form.cleaned_data['password']
        user = auth.authenticate(username=self.username, password=self.password)
        super(DoctorCreate, self).form_valid(form)
        if user is not None:
            auth.login(request, user)
            return redirect(reverse("doctors:doctor_profile", args=[new_doctor]))

        else:
            form.login_error = 'Користувач не знайдений! Можливо Ви забули пароль?'
        self.request.user = user
        return redirect(reverse("doctors:doctor_profile", args=[new_doctor]))
    '''

    def form_valid(self, form):
        self.username = form.cleaned_data['username']
        self.password = form.cleaned_data['password']
        user = auth.authenticate(username=self.username, password=self.password)
        if user is not None:
            auth.login(self.request, user)
            return redirect(reverse("doctors:doctors"))

        else:
            self.form_errors = 'Користувач не знайдений! Можливо Ви забули пароль?'
        #super(LoginForm, self).form_valid(form)
        return redirect(reverse("accounts:login"))

    def get_context_data(self, **kwargs):
        context = super(LoginForm, self).get_context_data(**kwargs)
        #
        context['form_errors'] = self.form_errors
        return context


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
    try:
        args['comments'] = Comment.objects.filter(user_id=user.id)
    except:
        args['comments'] = {}


    return render_to_response("accounts/login.html", args)


#    return render_to_response("accounts/login.html", {"user": request.user, "photo": photo})


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login")