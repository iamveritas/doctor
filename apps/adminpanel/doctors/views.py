from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import Doctor

from apps.adminpanel.doctors.forms import DoctorForm

def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:doctors:list"))


class DoctorsList(generic.ListView):
    context_object_name = "doctors"
    model = Doctor
    template_name = "adminpanel/doctors/list.html"
    paginate_by = 2


class AddDoctor(generic.CreateView):

    form = DoctorForm
    model = Doctor
    template_name = "adminpanel/doctors/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateDoctor(generic.UpdateView):

    form = DoctorForm
    model = Doctor
    template_name = "adminpanel/doctors/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteDoctor(generic.DeleteView):

    model = Doctor
    template_name = "adminpanel/doctors/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:doctors:list")