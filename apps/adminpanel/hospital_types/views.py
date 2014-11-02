from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import HospitalType
from apps.adminpanel.hospital_types.forms import HospitalTypeForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:hospital_types:list"))


class HospitalTypesList(generic.ListView):

    context_object_name = "hospital_types"
    model = HospitalType
    template_name = "adminpanel/hospital_types/list.html"


class AddHospitalType(generic.CreateView):

    form = HospitalTypeForm
    model = HospitalType
    template_name = "adminpanel/hospital_types/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateHospitalType(generic.UpdateView):

    form = HospitalTypeForm
    model = HospitalType
    template_name = "adminpanel/hospital_types/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteHospitalType(generic.DeleteView):

    model = HospitalType
    template_name = "adminpanel/hospital_types/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:regions:list")