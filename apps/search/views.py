# -*-coding:utf8-*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect, render
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, RequestContext
from apps.internal.models import Doctor, Recommendation, Comment, Hospital, Speciality
#from django.core.exceptions import ObjectDoesNotExist
#from django.db import IntegrityError
#from django.http.response import Http404
#from django.http import HttpResponse, HttpResponseRedirect
from apps.doctors.forms import DoctorForm, HospitalForm, CommentForm
from django.views.generic import ListView, TemplateView

from apps.internal.models import Doctor
from django.db.models import Q


class SearchView(ListView):

    model = Doctor
    context_object_name = 'doctors'
    template_name = "search/index.html"
    queryset = Doctor.objects.all().order_by('-recommend_yes')
    paginate_by = 4

    def get(self, request):
        # опрацьовуємо запити пошуку
        name = request.GET.get('name', '')
        speciality = int(request.GET.get('speciality', ''))
        # вибираємо всі спеціальності лікарів для форми пошуку
        specialities = Speciality.objects.all()
        doctors = Doctor.objects.filter(Q(last_name=name) | Q(speciality=speciality)).order_by('-recommend_yes')
        return render(request, "search/index.html", {'doctors': doctors, 'specialities': specialities})


class HomeView(TemplateView):

    template_name = "search/home.html"

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        # передаємо у context об’єкти Specialities
        context['specialities'] = Speciality.objects.all()
        return context
