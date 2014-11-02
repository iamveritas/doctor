from django.conf.urls import *

from django.contrib.auth.decorators import login_required

from apps.adminpanel.users import views


urlpatterns = patterns("",
    url(r"^$", login_required(views.UsersList.as_view()),
        name="list"),
    url(r"^add/$", view=login_required(views.AddUser.as_view()),
        name="add-user"),
    url(r"^update/(?P<pk>\d+)/$", view=login_required(views.UpdateUser.as_view()),
        name="update-user"),
    url(r"^delete/(?P<pk>\d+)/$", view=login_required(views.DeleteUser.as_view()),
        name="delete-user"),

)