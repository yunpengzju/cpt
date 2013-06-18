from django.shortcuts import render_to_response
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import global_settings  
from django.contrib import auth
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

def index(request):
    return render_to_response('index.html',context_instance=RequestContext(request))

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/register")
    else:
        form = UserCreationForm()
    return render_to_response("registration/register.html", 
        locals(), context_instance=RequestContext(request)
    )

def logout_view(request):
    auth.logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect("/index")
