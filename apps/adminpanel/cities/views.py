from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import City
from apps.adminpanel.cities.forms import CityForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:cities:list"))


class CitiesList(generic.ListView):

    context_object_name = "cities"
    model = City
    template_name = "adminpanel/cities/list.html"


class AddCity(generic.CreateView):

    form = CityForm
    model = City
    template_name = "adminpanel/cities/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateCity(generic.UpdateView):

    form = CityForm
    model = City
    template_name = "adminpanel/cities/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteCity(generic.DeleteView):

    model = City
    template_name = "adminpanel/cities/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:cities:list")