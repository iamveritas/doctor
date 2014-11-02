from django.views import generic
from django.core.urlresolvers import reverse

from apps.adminpanel import lib as admin_lib
from django.contrib.auth.models import User
from apps.adminpanel.users.forms import UserForm


def _get_redirect_url(request):
    return admin_lib.get_redirect_url(request, reverse("adminpanel:users:list"))


class UsersList(generic.ListView):

    context_object_name = "users"
    model = User
    template_name = "adminpanel/users/list.html"


class AddUser(generic.CreateView):

    form = UserForm
    model = User
    template_name = "adminpanel/users/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class UpdateUser(generic.UpdateView):

    form = UserForm
    model = User
    template_name = "adminpanel/users/add-update.html"

    def get_success_url(self):
        return _get_redirect_url(self.request)


class DeleteUser(generic.DeleteView):

    model = User
    template_name = "adminpanel/users/delete-confirm.html"

    def get_success_url(self):
        return reverse("adminpanel:users:list")