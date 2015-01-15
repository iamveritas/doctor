# -*- coding: utf-8 -*-
from django.shortcuts import render_to_response, redirect, render
from apps.accounts.forms import UserForm, LoginForm, UserDoctorForm
from django.contrib import auth
from django.core.context_processors import csrf
from apps.accounts.models import UserProfile, UserDoctor
from django.http import HttpResponseRedirect
from apps.internal.models import Comment, Doctor

from django.views.generic import ListView, DetailView, CreateView, UpdateView, FormView
from django.contrib.auth.models import User
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


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
            return redirect('/accounts/login')
        else:
            args['form'] = newuser_form
    return render_to_response('accounts/registration.html', args)


class LoginForm(FormView):
    """
    Перевіряє введені користувачем логін і пароль, якщо користувач з такими даними існує
    здійснює вхід і повертає особисту сторінку користувача, в іншому випадку повертає форму входу
    з повідомленням про помилку
    """

    template_name = 'accounts/login.html'
    form_class = LoginForm
    success_url = '/doctors/'

    def form_valid(self, form):
        self.username = form.cleaned_data['username']
        self.password = form.cleaned_data['password']
        user = auth.authenticate(username=self.username, password=self.password)
        if user is not None:
            auth.login(self.request, user)
        else:
            args = {'login_error': 'Користувач не знайдений! Можливо Ви забули пароль?',
                    'form':form}
            args.update(csrf(self.request))
            return render_to_response('accounts/login.html', args)
        return redirect(reverse("accounts:personal_page", args=[user.id]))


class UserDetail(DetailView):
    """
    Повертає детальну інформацію про користувача
    """

    model = User
    template_name = 'accounts/personal_page.html'
    context_object_name = 'user'

    # доступ додавати лікаря мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserDetail, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(UserDetail, self).get_context_data(**kwargs)
        # отримуємо отримуємо статус користувача
        if UserDoctor.objects.filter(user=self.request.user):
            context['user_status'] = 'doctor'
            # отримуємо об’єкт лікаря, який є користувачем
            doctor_id = UserDoctor.objects.get(user=self.request.user).doctor.id
            doctor = Doctor.objects.get(pk=doctor_id)
            # передаємо рейтинг лікаря у змінну rating
            context['rating'] = int(100*int(doctor.recommend_yes)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
            context['rating_minus'] = int(100*int(doctor.recommend_no)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
            # передаємо у context об’єкти Comment
            context['comments'] = Comment.objects.filter(doctor=self.object.id).filter(is_active=True).order_by('-created')
            # передаємо у context лікаря
            context['doctor'] = doctor

        else:
            context['user_status']  = 'user'
        # отримуємо коментарі, які залишив користувач
        context['user_comments'] = Comment.objects.filter(user=self.object.id).order_by('-created')
        # передаємо у context об’єкти Doctor для sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context фото користувача
        try:
            context['photo'] = UserProfile.objects.get(user=self.object.id).photo
        except Exception:
            pass
        return context


class UserDoctorCreate(CreateView   ):
    """
    Поєднує профіль користувача з профілем лікаря.
    Ідентифікує користувача як лікаря
    """
    form_class = UserDoctorForm
    model = UserDoctor
    success_url = '/doctors/'
    template_name = 'accounts/user_doctor.html'

    # доступ додавати лікаря мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(UserDoctorCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # перевіряємо, чи користувач ідентифікував себе як лікар раніше
        if UserDoctor.objects.filter(user=self.request.user.id):
            return redirect(reverse("accounts:personal_page", args=[self.request.user.id]))
        # вказуємо значення полів, які не можуть бути пустими і не відображаються у формі
        form.instance.user = self.request.user
        form.instance.status = False
        # перезавантажуємо метод form_valid() батьківського класу
        super(UserDoctorCreate, self).form_valid(form)
        return redirect(reverse("accounts:personal_page", args=[self.request.user.id]))

    def get_context_data(self, **kwargs):
        context = super(UserDoctorCreate, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        context['qq'] =  UserDoctor.objects.filter(user=self.request.user.id)
        return context



def doctor_user(request):
    args = {}
    form = DoctorUserForm()

    if request.method == 'POST':
        request.POST['user'] = request.user.id
        request.POST['status'] = False
        form = DoctorUserForm(request.POST)

        if form.is_valid():
#            doctor = form.save(commit=False)
            form.save()
            return HttpResponse('Thank you %s!<br/>'
                                '<a href="/">Повернутися на головну</a>' % request.user)
    args['form'] = form

    return render_to_response("doctors/user_doctor.html", args,
                              context_instance=RequestContext(request))




def login1(request):

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


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login")