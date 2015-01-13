from django.conf.urls import url, patterns

from apps.search.views import SearchView


urlpatterns = patterns("",
                       url("^$", SearchView.as_view(), name="index"),
                       )