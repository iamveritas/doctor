# -*-coding:utf8-*-
from django.shortcuts import render, render_to_response, get_object_or_404, RequestContext
from django.http.response import Http404
from django.http import HttpResponseRedirect
from apps.polls.models import Question, Choice


def poll(request, question_id='1'):

    try:
        question = get_object_or_404(Question, pk=question_id)
        args = {'question': question}
    except (KeyError, Choice.DoesNotExist):
        return Http404

    if question_id in request.COOKIES:
        return render_to_response("polls/results.html", args,
                          context_instance=RequestContext(request))

    if request.method == 'POST':

        try:
            selected_choice = question.choice_set.get(pk=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            args['message_errors'] = 'Ви нічого не обрали! Зробіть будь ласка вибір!'

        else:
            selected_choice.votes += 1
            selected_choice.save()
            response = HttpResponseRedirect("/")
            response.set_cookie(question_id, selected_choice.id, max_age=1209600)
            return response

    return render_to_response("polls/question.html", args,
                              context_instance=RequestContext(request))