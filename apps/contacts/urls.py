from django.conf.urls import url, patterns
from django.views.generic import TemplateView

from apps.contacts.views import ContactsView


urlpatterns = patterns("",
                       url("^$", ContactsView.as_view(), name="index"),
                       url("^feedback_form_success/$", TemplateView.as_view(
                           template_name="contacts/feedback_form_success.html"),
                           name="feedback_form_success"),
                       )