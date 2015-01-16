from django.conf.urls import patterns, include, url
import settings
from django.views.generic.base import TemplateView
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r"^$", include("apps.home.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^accounts/", include("apps.accounts.urls", namespace="accounts")),

#    url(r"^doctors/", include("apps.doctors.urls")),
    url(r"^contacts/", include("apps.contacts.urls", namespace="contacts")),
#    url(r"^contacts/", include('contact_form.urls')),

    url(r"^doctors/", include("apps.doctors.urls",  namespace="doctors")),
    url(r"^polls/", include("apps.polls.urls",  namespace="polls")),

    url(r"^regulations/", TemplateView.as_view(template_name='regulations/index.html'),  name="regulations"),

#    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
#    url(r"^accounts/", include("django.contrib.auth.urls")),
#    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^captcha/', include('captcha.urls')),
)
