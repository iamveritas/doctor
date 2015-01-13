# -*-coding:utf8-*-
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from django.views.generic import ListView, DetailView, CreateView, UpdateView
from django.shortcuts import redirect
from django.core.urlresolvers import reverse

from django.shortcuts import render_to_response, RequestContext
from apps.internal.models import Doctor, Recommendation, Comment, Hospital
#from django.core.exceptions import ObjectDoesNotExist
#from django.db import IntegrityError
#from django.http.response import Http404
#from django.http import HttpResponse, HttpResponseRedirect
from apps.doctors.forms import DoctorForm, HospitalForm, CommentForm
from django.views.generic import ListView

from apps.internal.models import Doctor


class SearchView(ListView):

    model = Doctor
    context_object_name = 'doctors'
    template_name = "search/results_of_search.html"
    queryset = Doctor.objects.all().order_by('-recommend_yes')
    paginate_by = 4

    #def search(request):
    #    query = request.GET['name']
    #    t = loader.get_template("search/results_of_search.html")
    #    c = Context({'query': query,})
    #    return HttpResponse(t.render(c))