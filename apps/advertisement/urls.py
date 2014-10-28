from django.conf.urls import *
from django.views.generic import TemplateView

urlpatterns = patterns("",
    url("^$", TemplateView.as_view(template_name="advertisement/index.html"),
        name="advertisement"),
)