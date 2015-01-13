from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',

    url(r"^$", include("apps.home.urls")),
    url(r'^admin/', include(admin.site.urls)),
    url(r"^accounts/", include("apps.accounts.urls", namespace="accounts")),


    url(r"^contacts/", include("apps.contacts.urls", namespace="contacts")),


    url(r"^doctors/", include("apps.doctors.urls",  namespace="doctors")),
    url(r"^polls/", include("apps.polls.urls",  namespace="polls")),

#    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
#    url(r"^accounts/", include("django.contrib.auth.urls")),
#    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^captcha/', include('captcha.urls')),

    url(r"^search/", include("apps.search.urls", namespace="search")),
)
