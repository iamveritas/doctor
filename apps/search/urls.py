from django.conf.urls import url, patterns
from apps.search.views import SearchView, HomeView


urlpatterns = patterns("",
    url("^$", SearchView.as_view(), name="index"),
    url("^home$", HomeView.as_view(), name="home"),
)