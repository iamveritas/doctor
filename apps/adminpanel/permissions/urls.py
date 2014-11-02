from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.permissions import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.PermissionsList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddPermission.as_view()),
        name="add-permission"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdatePermission.as_view()),
        name="update-permission"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeletePermission.as_view()),
        name="delete-permission"),

)