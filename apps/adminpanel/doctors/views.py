from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import Doctor

def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:doctors:list"))


class DoctorList(generic.ListView):
    context_object_name = "doctors"
    model = Doctor
    template_name = "adminpanel/doctors/doctors.html"