# -*-coding:utf8-*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, RequestContext, get_object_or_404
from apps.internal.models import Doctor, Recommendation, Comment, Hospital, CommentAnswer
#from django.core.exceptions import ObjectDoesNotExist
#from django.db import IntegrityError
from django.http.response import Http404
#from django.http import HttpResponse, HttpResponseRedirect
from apps.doctors.forms import DoctorForm, HospitalForm, CommentForm, CommentAnswerForm

from apps.accounts.models import UserProfile, UserSetting

class HospitalCreate(CreateView):
    """
    Повертає форму для створення нової клініки
    """

    model = Hospital
    template_name = 'doctors/hospital_add.html'
    form_class = HospitalForm
    success_url = '/doctors/add/'

    # доступ додавати клініку мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(HospitalCreate, self).dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(HospitalCreate, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        return context


class DoctorCreate(CreateView):
    """
    Повертає форму для створення нового лікаря
    """

    model = Doctor
    template_name = 'doctors/doctor_add.html'
    form_class = DoctorForm
    success_url = '/doctors/'

    # доступ додавати лікаря мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(DoctorCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # вказуємо значення полів, які не можуть бути пустими і не відображаються у формі
        form.instance.user = self.request.user
        form.instance.is_active = False
        form.instance.recommend_no = 0
        form.instance.recommend_yes = 0
        # перезавантажуємо метод form_valid() батьківського класу
        super(DoctorCreate, self).form_valid(form)
        # отримуємо id новоствореного лікаря, щоб перейти на його сторінку, після вдалого збереження даних про нього в БД
        new_doctor = Doctor.objects.order_by('-created')[0].id
        return redirect(reverse("doctors:doctor_profile", args=[new_doctor]))

    def get_context_data(self, **kwargs):
        context = super(DoctorCreate, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        return context


class DoctorList(ListView):
    """
    Повертає список лікарів відсортований по рекомендаціях (recommend_yes)
    """

    model = Doctor
    context_object_name = 'doctors'
    template_name = 'doctors/doctors.html'
    queryset = Doctor.objects.order_by('-recommend_yes')
    paginate_by = 16


class DoctorReviewList(ListView):
    """
    Повертає список коментарів відсортованих по даті додавання
    """

    model = Comment
    context_object_name = 'comments'
    template_name = 'doctors/reviews.html'
    paginate_by = 2

    def get_queryset(self):
        """
        Повертає коментарі заданого лікаря
        """
        return Comment.objects.filter(doctor=self.kwargs['pk']).filter(is_active=True).order_by('-created')

    def get_context_data(self, **kwargs):
        context = super(DoctorReviewList, self).get_context_data(**kwargs)
        # отримуємо об’єкт лікаря
        doctor = Doctor.objects.get(pk=self.kwargs['pk'])
        # передаємо у context об’єкти Doctor для sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context об’єкт лікаря, для якого додається рейтигн
        context['doctor'] = doctor
        # передаємо у context відгуки на коментарі
        context['comment_answers'] = CommentAnswer.objects.filter(doctor=doctor.id).filter(is_active=True).order_by('-created')
        # передаємо у context об’єкт лікаря, для якого додається рейтигн
        #context['form'] = CommentForm()
        # передаємо у context фото користувача
        if UserProfile.objects.filter(user=doctor.userdoctor.user):
            context['photo'] = UserProfile.objects.get(user=doctor.userdoctor.user).photo
        elif UserSetting.objects.filter(user=doctor.userdoctor.user):
            context['photo'] = UserSetting.objects.get(user=doctor.userdoctor.user).photo
        else:
            context['photo'] = False
        return context


class DoctorDetail(DetailView):
    """
    Повертає детальну інформацію про лікаря
    """

    model = Doctor
    template_name = 'doctors/home.html'
    context_object_name = 'doctor'

    def get_context_data(self, **kwargs):
        context = super(DoctorDetail, self).get_context_data(**kwargs)
        # отримуємо об’єкт лікаря, для якого додається рейтигн
        doctor = Doctor.objects.get(pk=self.kwargs['pk'])
        # перевіряємо чи була спроба рекомендації і пробуємо записати її в БД
        try:
            if not Recommendation.objects.filter(user=self.request.user, doctor=doctor.id):
                if self.kwargs['recommend'] == 'yes':
                    doctor.recommend_yes +=1
                    self.recommend = 1
                elif self.kwargs['recommend'] == 'no':
                    doctor.recommend_no +=1
                    self.recommend = 0
                Recommendation(user_id=self.request.user.id, doctor_id=doctor.id, recommendation=self.recommend).save()
                doctor.save()
        except:
            pass
        # передаємо рейтинг лікаря у змінну rating
        context['rating'] = int(100*int(doctor.recommend_yes)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        context['rating_minus'] = int(100*int(doctor.recommend_no)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        # передаємо у context об’єкти Comment, CommentAnswer, Doctor
        context['comments'] = Comment.objects.filter(doctor=self.object.id).filter(is_active=True).order_by('-created')[:5]
        context['comment_answers'] = CommentAnswer.objects.filter(doctor=self.object.id).filter(is_active=True).order_by('-created')
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context об’єкт лікаря, для якого додається рейтигн
        context['doctor'] = doctor
        # передаємо у context об’єкт лікаря, для якого додається рейтигн
        context['form'] = CommentForm()
        # передаємо у context фото користувача, якщо лікар ідентифікований користувачем
        try:
            if UserProfile.objects.filter(user=doctor.userdoctor.user.id):
                context['photo'] = UserProfile.objects.get(user=doctor.userdoctor.user.id).photo
        except Exception:
            pass

        try:
            if UserSetting.objects.filter(user=doctor.userdoctor.user.id):
                context['photo'] = UserSetting.objects.get(user=doctor.userdoctor.user.id).photo
            else:
                context['photo'] = False
        except Exception:
            pass
        return context


class CommentCreate(CreateView):
    """
    Повертає форму для створення нового коментаря
    """

    model = Comment
    template_name = 'doctors/comment_update.html'
    form_class = CommentForm
    success_url = '/doctors/'


    # доступ додавати лікаря мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CommentCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # вказуємо значення полів, які не можуть бути пустими і не відображаються у формі
        form.instance.user = self.request.user
        form.instance.is_active = False
        form.instance.doctor = Doctor.objects.get(pk=self.get_queryset().id)
        # перезавантажуємо метод form_valid() батьківського класу
        super(CommentCreate, self).form_valid(form)
        return render(self.request, 'doctors/comment_add_success.html', {'pk': self.get_queryset().id})

    def form_invalid(self, form):
        """
        Якщо форма не валідна (користувач спробував відправити порожню форму,
        здійснюється редірект на сторінку лікаря.
        """
        super(CommentCreate, self).form_invalid(form)
        return redirect(reverse("doctors:doctor_profile", args=[self.get_queryset().id]))

    def get_queryset(self):
        """
        Повертає об’єкт лікаря, для якого додається коментар
        """
        return Doctor.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # передаємо у context об’єкт Doctor, для якого додаємо коментар
        doctor = Doctor.objects.get(pk=self.get_queryset().id)
        context['doctor'] = doctor
        # передаємо рейтинг лікаря у змінну rating
        context['rating'] = int(100*int(doctor.recommend_yes)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        context['rating_minus'] = int(100*int(doctor.recommend_no)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        return context


class CommentAnswerCreate(CreateView):
    """
    Повертає форму для створення коментаря на відгук
    """

    model = CommentAnswer
    template_name = 'doctors/comment_add.html'
    form_class = CommentAnswerForm
    success_url = '/doctors/'

    # доступ тільки для зареєстрованих користувачів
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CommentAnswerCreate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # вказуємо значення полів, які не можуть бути пустими і не відображаються у формі
        form.instance.is_active = True
        form.instance.comment = Comment.objects.get(pk=self.kwargs['pk'])
        form.instance.doctor = form.instance.comment.doctor
        # перезавантажуємо метод form_valid() батьківського класу
        super(CommentAnswerCreate, self).form_valid(form)
        return redirect(reverse("doctors:doctor_profile", args=[form.instance.doctor.id]))

    def get_context_data(self, **kwargs):
        context = super(CommentAnswerCreate, self).get_context_data(**kwargs)
        # передаємо у context об’єкт Doctor, для якого додаємо коментар
        doctor = Comment.objects.get(pk=self.kwargs['pk']).doctor
        context['doctor'] = doctor
        # передаємо рейтинг лікаря у змінну rating
        context['rating'] = int(100*int(doctor.recommend_yes)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        context['rating_minus'] = int(100*int(doctor.recommend_no)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context відгук, що коментується
        context['comment'] = Comment.objects.get(pk=self.kwargs['pk'])
        return context


class CommentAnswerUpdate(UpdateView):
    """
    Повертає форму для редагування коментаря на відгук
    """

    model = CommentAnswer
    template_name = 'doctors/comment_add.html'
    form_class = CommentAnswerForm
    success_url = '/doctors/'

    # доступ тільки для зареєстрованих користувачів
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        # перевіряємо чи користувач має право редагувати коментар
        doctor = get_object_or_404(CommentAnswer, pk=self.kwargs['pk']).doctor.userdoctor.user.id
        if not self.request.user.id == doctor:
            raise Http404
        return super(CommentAnswerUpdate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # вказуємо значення полів, які не можуть бути пустими і не відображаються у формі
        form.instance.is_active = True
        form.instance.comment = CommentAnswer.objects.get(pk=self.kwargs['pk']).comment
        form.instance.doctor = form.instance.comment.doctor
        # перезавантажуємо метод form_valid() батьківського класу
        super(CommentAnswerUpdate, self).form_valid(form)
        return redirect(reverse("doctors:doctor_profile", args=[form.instance.doctor.id]))

    def get_context_data(self, **kwargs):
        context = super(CommentAnswerUpdate, self).get_context_data(**kwargs)
        # передаємо у context об’єкт Doctor, для якого додаємо коментар
        doctor = CommentAnswer.objects.get(pk=self.kwargs['pk']).doctor
        context['doctor'] = doctor
        # передаємо рейтинг лікаря у змінну rating
        context['rating'] = int(100*int(doctor.recommend_yes)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        context['rating_minus'] = int(100*int(doctor.recommend_no)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context відгук, що коментується
        context['comment'] = CommentAnswer.objects.get(pk=self.kwargs['pk']).comment
        return context


class CommentUpdate(UpdateView):
    """
    Повертає заповнену форму для редагування коментаря
    Після успішного редагування коментар відправляється на перевірку і здійнюється
    рерірект на сторінку лікаря
    """

    model = Comment
    template_name = 'doctors/comment_update.html'
    form_class = CommentForm
    success_url = '/doctors/'

    # доступ додавати лікаря мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        # перевіряємо чи користувач має право редагувати відгук
        creater = get_object_or_404(Comment, pk=self.kwargs['pk']).user_id
        if not self.request.user.id == creater:
            raise Http404
        return super(CommentUpdate, self).dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        # вказуємо значення поля is_active = False, щоб відправити коментар на перевірку
        form.instance.is_active = False
        # перезавантажуємо метод form_valid() батьківського класу
        super(CommentUpdate, self).form_valid(form)
        # отримуємо id лікаря, для якоро редагується коментар, щоб після успішного редагування
        # зробити редірект на сторінку лікаря
        doctor = str(Comment.objects.get(pk=self.kwargs['pk']).doctor.id)
        return render(self.request, 'doctors/comment_update_success.html', {'pk': doctor})

    def get_context_data(self, **kwargs):
        context = super(CommentUpdate, self).get_context_data(**kwargs)
        # передаємо у context об’єкт Doctor, для якого додаємо коментар
        doctor = Comment.objects.get(pk=self.kwargs['pk']).doctor
        context['doctor'] = doctor
        # передаємо рейтинг лікаря у змінну rating
        context['rating'] = int(100*int(doctor.recommend_yes)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        context['rating_minus'] = int(100*int(doctor.recommend_no)/(int(doctor.recommend_yes) + int(doctor.recommend_no)+0.001)+0.5)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        return context
