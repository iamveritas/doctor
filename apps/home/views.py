from django.shortcuts import render_to_response, RequestContext

#from apps.internal.models import Customer, Review, Project
#from apps.contacts.forms import FeedbackForm


def index(request):

    return render_to_response("home/index.html", context_instance=RequestContext(request))