# -*-coding:utf8-*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, RequestContext
from apps.internal.models import Doctor, Recommendation, Comment, Hospital
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http.response import Http404
from django.http import HttpResponse, HttpResponseRedirect
from apps.doctors.forms import DoctorForm, DoctorUserForm, HospitalForm, CommentForm


class HospitalCreate(CreateView):
    """
    Повертає форму для створення нової клініки
    """

    model = Hospital
    template_name = 'doctors/add_hospital.html'
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
    template_name = 'doctors/add_update.html'
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
    queryset = Doctor.objects.all().order_by('-recommend_yes')
    paginate_by = 4


class DoctorDetail(DetailView):
    """
    Повертає детальну інформацію про лікаря
    """

    model = Doctor
    template_name = 'doctors/doctor_profile.html'
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
        # передаємо у context об’єкти Comment, Doctor
        context['comments'] = Comment.objects.filter(doctor=self.object.id).filter(is_active=True).order_by('-created')
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context об’єкт лікаря, для якого додається рейтигн
        context['doctor'] = doctor
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

    return render_to_response("doctors/doctor_user.html", args,
                              context_instance=RequestContext(request))



class CommentCreate(CreateView):
    """
    Повертає форму для створення нового коментаря
    """

    model = Comment
    template_name = 'doctors/add_comment.html'
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
        return redirect(reverse("doctors:doctor_profile", args=[self.get_queryset().id]))

    def get_queryset(self):
        """
        Повертає об’єкт лікаря, для якого додається коментар
        """
        return Doctor.objects.get(pk=self.kwargs['pk'])

    def get_context_data(self, **kwargs):
        context = super(CommentCreate, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Doctor для  елементів sidebar
        context['doctors'] = Doctor.objects.order_by('-recommend_yes')[:6]
        # передаємо у context об’єкт Doctor, для якого додаємо коментар
        context['doctor'] = Doctor.objects.get(pk=self.get_queryset().id)
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

    # доступ додавати лікаря мають тільки зареєстровані користувачі
    @method_decorator(login_required())
    def dispatch(self, request, *args, **kwargs):
        return super(CommentUpdate, self).dispatch(request, *args, **kwargs)

    def get_success_url(self):
        # отримуємо id лікаря, для якоро редагується коментар, щоб після успішного редагування
        # зробити редірект на сторінку лікаря
        doctor = str(Comment.objects.get(pk=self.kwargs['pk']).doctor.id)
        return u'/doctors/'+doctor

    def form_valid(self, form):
        # вказуємо значення поля is_active = False, щоб відправити коментар на перевірку
        form.instance.is_active = False
        # перезавантажуємо метод form_valid() батьківського класу
        super(CommentUpdate, self).form_valid(form)
        # отримуємо id лікаря, для якоро редагується коментар, щоб після успішного редагування
        # зробити редірект на сторінку лікаря
        doctor = str(Comment.objects.get(pk=self.kwargs['pk']).doctor.id)
        return redirect(reverse("doctors:doctor_profile", args=[doctor]))
