from django.conf.urls import patterns, include, url
from apps.polls import views


urlpatterns = patterns("",
    url(r'^(?P<question_id>\d+)/$',views.poll, name="poll"),
    url(r'^$',views.poll, name="poll"),
)