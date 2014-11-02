from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import Hospital
from apps.adminpanel.hospitals.forms import HospitalForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:hospitals:list"))


class HospitalsList(generic.ListView):

    context_object_name = "hospitals"
    model = Hospital
    template_name = "adminpanel/hospitals/list.html"
    paginate_by = 1


class AddHospital(generic.CreateView):

    form = HospitalForm
    model = Hospital
    template_name = "adminpanel/hospitals/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateHospital(generic.UpdateView):

    form = HospitalForm
    model = Hospital
    template_name = "adminpanel/hospitals/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteHospital(generic.DeleteView):

    model = Hospital
    template_name = "adminpanel/hospitals/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:hospitals:list")