from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r"^$", "apps.home.views.index", name="home"),
    url(r"^accounts/", include("django.contrib.auth.urls")),
    url(r"^rules/", include("apps.rules.urls", namespace="rules")),
    url(r"^advertisement/", include("apps.advertisement.urls", namespace="advertisement")),
    url(r"^faq/", include("apps.faq.urls", namespace="faq")),
    url(r"^contacts/", include("apps.contacts.urls", namespace="contacts")),
    #url(r"^admin/", include(admin.site.urls)),
    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT})
)
