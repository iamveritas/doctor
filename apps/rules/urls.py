from django.conf.urls import *
from django.views.generic import TemplateView

urlpatterns = patterns("",
    url("^$", TemplateView.as_view(template_name="rules/index.html"),
        name="index"),
)