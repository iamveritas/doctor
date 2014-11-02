from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from django.contrib.auth.models import Permission
from apps.adminpanel.permissions.forms import PermissionForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:permissions:list"))


class PermissionsList(generic.ListView):

    context_object_name = "permissions"
    model = Permission
    template_name = "adminpanel/permissions/list.html"


class AddPermission(generic.CreateView):

    form = PermissionForm
    model = Permission
    template_name = "adminpanel/permissions/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdatePermission(generic.UpdateView):

    form = PermissionForm
    model = Permission
    template_name = "adminpanel/permissions/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeletePermission(generic.DeleteView):

    model = Permission
    template_name = "adminpanel/permissions/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:permissions:list")