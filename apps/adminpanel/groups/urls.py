from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.groups import views


urlpatterns = patterns("",
    url(r"^$", view=login_required(views.GroupsList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddGroup.as_view()),
        name="add-group"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateGroup.as_view()),
        name="update-group"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteGroup.as_view()),
        name="delete-group"),

)