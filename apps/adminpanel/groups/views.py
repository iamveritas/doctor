from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from django.contrib.auth.models import Group
from apps.adminpanel.groups.forms import GroupForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:groups:list"))


class GroupsList(generic.ListView):

    context_object_name = "groups"
    model = Group
    template_name = "adminpanel/groups/list.html"


class AddGroup(generic.CreateView):

    form = GroupForm
    model = Group
    template_name = "adminpanel/groups/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateGroup(generic.UpdateView):

    form = GroupForm
    model = Group
    template_name = "adminpanel/groups/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteGroup(generic.DeleteView):

    model = Group
    template_name = "adminpanel/groups/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:groups:list")