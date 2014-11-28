# -*-coding:utf8-*-
from django.shortcuts import render_to_response, redirect, RequestContext
from apps.internal.models import Doctor, Recommendation
from django.core.exceptions import ObjectDoesNotExist
from django.db import IntegrityError
from django.http.response import Http404
from django.views import generic
from apps.adminpanel.doctors.forms import DoctorForm


class AddDoctor(generic.CreateView):

    form = DoctorForm
    model = Doctor
    template_name = "doctor_page/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


def doctors(request):
    args = {}
    args['doctors'] = Doctor.objects.all()
    if not args['doctors']:
        args['doctors'] = 'Немає лікарів'
    return render_to_response("doctor_page/doctors.html", args,
                              context_instance=RequestContext(request))


def doctor_profile(request, doctor_id):
    try:
        args = {}
        args['doctor'] = Doctor.objects.get(id=doctor_id)
    except ObjectDoesNotExist:
        raise Http404
    return render_to_response("doctor_page/doctor_profile.html", args,
                              context_instance=RequestContext(request))


def recommendation(request, doctor_id, recommend):
    try:
        args = {}
        doctor = Doctor.objects.get(id=doctor_id)
        args['doctor'] = doctor

        if (request.user is not None and
            request.user.is_active and
            not Recommendation.objects.filter(user=request.user.id, doctor=doctor.id)):

            if recommend == 'yes':
                doctor.recommend_yes += 1
                recommend = 1
            elif recommend == 'no':
                doctor.recommend_no += 1
                recommend = 0

            Recommendation(user_id=request.user.id, doctor_id=doctor.id, recommendation=recommend).save()
            doctor.save()

    except (ObjectDoesNotExist, IntegrityError):
        raise Http404

    return render_to_response("doctor_page/doctor_profile.html", args,
                              context_instance=RequestContext(request))
