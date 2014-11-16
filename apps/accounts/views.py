from django.shortcuts import render_to_response, redirect
from apps.accounts.forms import UserForm
#from django.contrib import auth
from django.core.context_processors import csrf


def registration(request):
    args = {}
    args.update(csrf(request))
    newuser_form = UserForm()
    args['form'] = newuser_form
    if request.POST:
        newuser_form = UserForm(request.POST)

        if newuser_form.is_valid():
            newuser_form.save()
#            newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
#                                        password=newuser_form.cleaned_data['password1'])
#            auth.login(request, newuser)
            return redirect('/')
        else:
            args['form'] = newuser_form
    return render_to_response('accounts/registration.html', args)
