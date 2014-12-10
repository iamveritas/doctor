from django.conf.urls import patterns, include, url
import settings

from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^$", "apps.home.views.index", name="home"),
    url(r"^accounts/", include("apps.accounts.urls")),
    url(r"^doctors/", include("apps.doctor_page.urls")),
    url(r"^contacts/", include("apps.contacts.urls", namespace="contacts")),
#    url(r"^contacts/", include('contact_form.urls')),
#    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
#    url(r"^accounts/", include("django.contrib.auth.urls")),
#    url(r"^adminpanel/", include("apps.adminpanel.urls", namespace="adminpanel")),
    (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
        'document_root': settings.MEDIA_ROOT}),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^captcha/', include('captcha.urls')),
)
