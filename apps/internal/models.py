from django.db import models
from django.utils.translation import ugettext_lazy as _


PROJECT_TYPE_CHOICES = (
    ("web_project", _("Web Project")),
    ("stand_alone_application", _("Stand Alone Application")),
    ("cloud_application", _("Cloud Application"))
)


class Doctor(models.Model):

    first_name = models.CharField(_("First Name"), blank=False, max_length=20)
    last_name = models.CharField(_("Last Name"), blank=False, max_length=20)
    email = models.EmailField(_("Email"), blank=False, max_length=50)
    phone = models.CharField(_("Phone"), blank=True, max_length=20)
    skype = models.CharField(_("Skype"), blank=True, max_length=30)
    summary = models.TextField(
        _("Developer's Summary Profile Info"), max_length=700, blank=True)
    linkedin_profile = models.URLField(_("LinkedIn URL"), blank=True)
    github_username = models.CharField(_("GitHub User Name"), blank=True,
                                       max_length=20)
    resume_file = models.FileField(_("Resume"), upload_to="developer_resume/",
                                   null=True, blank=True)

    def __unicode__(self):
        return u"%s %s" % (self.first_name, self.last_name)