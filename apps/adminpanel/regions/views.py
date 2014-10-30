from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from apps.internal.models import Region
from apps.adminpanel.regions.forms import RegionForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:regions:list"))


class RegionsList(generic.ListView):

    context_object_name = "regions"
    model = Region
    template_name = "adminpanel/regions/list.html"


class AddRegion(generic.CreateView):

    form = RegionForm
    model = Region
    template_name = "adminpanel/regions/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateRegion(generic.UpdateView):

    form = RegionForm
    model = Region
    template_name = "adminpanel/regions/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteRegion(generic.DeleteView):

    model = Region
    template_name = "adminpanel/regions/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:regions:list")