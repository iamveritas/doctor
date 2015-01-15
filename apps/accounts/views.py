# -*- coding: utf-8 -*-
from django.shortcuts import render, render_to_response, redirect
from apps.accounts.forms import (UserForm, LoginForm, UserDoctorForm, UserSettingsForm,
                                 UserSettingsDocPhotoForm, UserSettingsDocForm,)
from django.contrib import auth
from django.core.context_processors import csrf
from apps.accounts.models import UserProfile, UserDoctor, UserSetting
from django.http import HttpResponseRedirect, HttpResponse
from apps.internal.models import Comment, Doctor, CommentAnswer

from django.views.generic import DetailView, ListView, CreateView, FormView
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from settings import MEDIA_ROOT

class UserCreate(CreateView):
    """
    Повертає реєстраційну форму
    """

    model = User
    template_name = 'accounts/registration.html'
    form_class = UserForm
    success_url = '/login/'

    def form_valid(self, form):
        super(UserCreate, self).form_valid(form)
        form_login = LoginForm()
        args = {'success_registration': 'Реєстрація пройшла успішно. Введіть логін і пароль, щоб увійти на сайт.',
                'form':form_login}
        args.update(csrf(self.request))
        return render_to_response('accounts/login.html', args)


class UserLogin(FormView):
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
    template_name = 'accounts/home.html'
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
            context['comments'] = Comment.objects.filter(doctor=doctor_id).filter(is_active=True).order_by('-created')[:5]
            # передаємо у context лікаря
            context['doctor'] = doctor

        else:
            context['user_status'] = 'user'
        # перевіряємо чи користувач зареєструвався через соц мережі
        if UserProfile.objects.filter(user=self.object.id):
            context['nonsocial'] = False
        else:
            context['nonsocial'] = True
        # отримуємо коментарі, які залишив користувач
        context['user_comments'] = Comment.objects.filter(user=self.object.id).order_by('-created')[:5]
        # передаємо у context об’єкти Doctor для sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context коментарі до відгуків
        context['comment_answers'] = CommentAnswer.objects.filter(is_active=True).order_by('-created')
        # передаємо у context фото користувача
        if UserProfile.objects.filter(user=self.object.id):
            context['photo'] = UserProfile.objects.get(user=self.object.id).photo
        elif UserSetting.objects.filter(user=self.request.user.id):
            context['photo'] = UserSetting.objects.get(user=self.request.user.id).photo
        else:
            context['photo'] = False
        return context


class UserReviewList(ListView):
    """
    Повертає список коментарів користувача відсортованих по даті додавання
    """

    model = Comment
    context_object_name = 'user_comments'
    template_name = 'accounts/reviews_from_me_all.html'
    paginate_by = 2

    def get_queryset(self):
        """
        Повертає коментарі активного користувача
        """
        return Comment.objects.filter(user=self.request.user).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(UserReviewList, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Doctor для sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context коментарі до відгуків
        context['comment_answers'] = CommentAnswer.objects.filter(is_active=True).order_by('-created')
        return context


class UserDoctorCreate(CreateView):
    """
    Поєднує профіль користувача з профілем лікаря.
    Ідентифікує користувача як лікаря
    """
    form_class = UserDoctorForm
    model = UserDoctor
    success_url = '/doctors/'
    template_name = 'accounts/user_is_doctor_form.html'

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


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/accounts/login")


def user_settings(request):
    """
    Повертає форму для редагування даних користувача (ім’я, прізвище) і додавання/оновлення фото.
    """
    # передаємо у context об’єкти Doctor для  елементів sidebar
    doctors = Doctor.objects.order_by('-recommend_yes')[:6]
    args = {'doctors': doctors}
    # створюємо об’єкт користувача
    user = User.objects.get(pk=request.user.id)
    # перевіряємо чи була відправлена форма
    if request.method == 'POST':
        # створюємо об’єкт форми
        form = UserSettingsForm(request.POST, request.FILES)
        # передаємо у форму обов’язкове поле user
        form.instance.user = request.user
        if form.is_valid():
            # Якщо форма валідна, зберігаємо ім’я і прізвище користувача у таблицю User
            user.last_name = form.cleaned_data["last_name"]
            user.first_name = form.cleaned_data["first_name"]
            user.save()
            # якщо дані про користувача уже є у таблиці UserSetting, то редагуємо їх, в іншому випадку
            # додаємо новий запис
            if  UserSetting.objects.filter(user=request.user):
                user_setting = UserSetting.objects.get(user=request.user)
                if form.cleaned_data['photo']:
                    user_setting.photo = form.cleaned_data['photo']
                user_setting.last_name = form.cleaned_data['last_name']
                user_setting.first_name = form.cleaned_data['first_name']
                user_setting.save()
            else:
                form.save()
    else:
        # якщо форма не була відправлена, заповнюємо її даними користувача з таблиці User
        data = {'last_name': user.last_name,
                'first_name': user.first_name}
        form = UserSettingsForm(data)

    args['form'] = form
  # якщо фото користувача уже збережено у БД, витягуємо об’єкт з таблиці UserSetting для активного користувача
    # і передаємо фото у контекст
    if UserSetting.objects.filter(user=request.user.id):
        photo = UserSetting.objects.get(user=request.user.id)
        args['photo'] = photo.photo

    return  render(request, 'accounts/settings.html', args)


def user_settings_doctor(request):
    """
    Повертає форму для редагування даних користувача (лікаря) і додавання/оновлення фото.
    """
    # передаємо у context об’єкти Doctor для  елементів sidebar
    doctors = Doctor.objects.order_by('-recommend_yes')[:6]
    # отримуємо об’єкт лікаря зв’язаного з користувачем
    doctor = request.user.userdoctor.doctor
    # перевіряємо чи була відправлена форма
    if request.method == 'POST':
        # створюємо об’єкт форми
        form = UserSettingsDocForm(request.POST, request.FILES)
        if form.is_valid():
            doctor.speciality = form.cleaned_data['speciality']
            doctor.hospitals = form.cleaned_data['hospitals']
            doctor.save()
            if  UserSetting.objects.filter(user=request.user):
                user_setting = UserSetting.objects.get(user=request.user)
                if form.cleaned_data['image']:
                    user_setting.photo = form.cleaned_data['image']
                user_setting.save()
            elif UserProfile.objects.filter(user=request.user):
                pass
            else:
                UserSetting.objects.create(user=request.user,
                                           photo=form.cleaned_data['image'],
                                           first_name=form.cleaned_data['first_name'],
                                           last_name=form.cleaned_data['larst_name'],
                                           )
    else:
        # якщо форма не була відправлена, заповнюємо її даними користувача з таблиці User
        hospitals = [hospital.id for hospital in doctor.hospitals.all()]
        data = {'speciality': doctor.speciality.id, 'hospitals': hospitals}
        form = UserSettingsDocForm(data)
    args = {'doctors': doctors, 'form': form}
    # якщо фото користувача уже збережено у БД, витягуємо об’єкт з таблиці UserSetting для активного користувача
    # і передаємо фото у контекст
    if UserSetting.objects.filter(user=request.user.id):
        photo = UserSetting.objects.get(user=request.user.id)
        args['photo'] = photo.photo
    return  render(request, 'accounts/settings.html', args)


"""
def user_settings(request):
    user = User.objects.get(pk=request.user.id)
    if  UserProfile.objects.filter(user=request.user):
        user_photo = UserProfile.objects.get(user=request.user)
        qq = 1
    else:
        user_photo = UserProfile(user=request.user, photo='')
        qq = 2
    if request.method == 'POST':
        form = UserSettingsForm(request.POST, request.FILES)
        if form.is_valid():
            user.first_name = form.cleaned_data["first_name"]
            user.last_name = form.cleaned_data["last_name"]
            user.save()
            #handle_uploaded_file(request.FILES['file'])
            user_photo.photo = request.FILES['photo'].name
            user_photo.save()

            file = request.FILES['photo']
            with open('%s/%s/%s' % (MEDIA_ROOT, 'user_photos', user_photo.photo), 'wb+') as fd:
                fd.write(file.read())
                fd.close()
            pp = 6
            #pp = dir(user_photo)
            pp = dir(request.FILES['photo'])
            #pp = request.FILES['photo'].name
        else:
            pp = 3
    else:
        data = {'first_name': user.first_name,
                'last_name': user.last_name,
                'photo': user_photo.photo}
        form = UserSettingsForm(data)
        pp = 1



    args = {'form': form, 'pp': pp}

    return  render(request, 'accounts/settings.html', args)
"""