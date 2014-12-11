from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.mail import send_mail

from django.views.decorators.http import require_http_methods
from django.utils.translation import ugettext as _
from django.template import loader, RequestContext, Context

from settings import FEEDBACK_EMAIL_RECEIVERS

from apps.contacts.forms import FeedbackForm
from apps.library.decorators import ajax_required
#from apps.library import json_response


def _handle_valid_feedback_form(form):

    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    email_text = form.cleaned_data["text"]

    email_message_tpl = loader.get_template("email/feedback_email.txt")
    email_message = email_message_tpl.render(Context({
        "user_name": name,
        "user_email": email,
        "message": email_text
    }))

    send_mail('From contacts page lykar.com.ua', email_message, 'info@lykar.com.ua',
              FEEDBACK_EMAIL_RECEIVERS, fail_silently=False)


class ContactsView(FormView):

    form_class = FeedbackForm
    template_name = "contacts/index.html"

    def form_valid(self, form):

        _handle_valid_feedback_form(form)

        return redirect(reverse("contacts:feedback_form_success"))