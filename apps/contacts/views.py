from django.views.generic import FormView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.template import loader, Context

from settings import FEEDBACK_EMAIL_RECEIVERS

from apps.contacts.forms import FeedbackForm


def _handle_valid_feedback_form(form):

    name = form.cleaned_data["name"]
    email = form.cleaned_data["email"]
    text = form.cleaned_data["text"]

    email_message_tpl = loader.get_template("contacts/feedback_email.txt")
    email_message = email_message_tpl.render(Context({
        "user_name": name,
        "user_email": email,
        "message": text,
    }))

    send_mail('LYKAR.COM.UA: from contacts page ', email_message, 'info@lykar.com.ua',
              FEEDBACK_EMAIL_RECEIVERS, fail_silently=False)


class ContactsView(FormView):

    form_class = FeedbackForm
    template_name = "contacts/index.html"

    def form_valid(self, form):

        _handle_valid_feedback_form(form)

        return redirect(reverse("contacts:feedback_form_success"))