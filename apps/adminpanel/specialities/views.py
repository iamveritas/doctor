from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import Speciality
from apps.adminpanel.specialities.forms import SpecialityForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:specialities:list"))


class SpecialitiesList(generic.ListView):

    context_object_name = "specialities"
    model = Speciality
    template_name = "adminpanel/specialities/list.html"


class AddSpeciality(generic.CreateView):

    form = SpecialityForm
    model = Speciality
    template_name = "adminpanel/specialities/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateSpeciality(generic.UpdateView):

    form = SpecialityForm
    model = Speciality
    template_name = "adminpanel/specialities/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteSpeciality(generic.DeleteView):

    model = Speciality
    template_name = "adminpanel/specialities/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:specialities:list")