from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import global_settings
from django.contrib import auth
from django.contrib.auth.decorators import permission_required

from cpt.contact.models import Contact
from cpt.contact.models import ContactForm

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS


@permission_required('contact.is_member', login_url="/login/")
def contact_list(request):
    result = Contact.objects.all()
    return render_to_response('contact/list.html', locals(), context_instance=RequestContext(request))


@permission_required('contact.is_member', login_url="/login/")
def contact_one(request, contact_id):
    try:
        result = Contact.objects.get(number=contact_id);
        return render_to_response('contact/one.html', locals(), context_instance=RequestContext(request))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/contact/')


@permission_required('contact.is_member', login_url="/login/")
def contact_me(request):
    try:
        isme = True
        result = ContactForm(instance=Contact.objects.get(nickname=request.user.username));
        return render_to_response('contact/one.html', locals(), context_instance=RequestContext(request))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/contact/')


@permission_required('contact.is_member', login_url="/login/")
def contact_edit(request):
    try:
        inst = Contact.objects.get(nickname=request.user.username)
        if request.method == 'POST':
            form = ContactForm(request.POST, instance=inst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/contact/me/')
        else:
            form = ContactForm(instance=inst);
        return render_to_response('contact/edit.html', locals(), context_instance=RequestContext(request))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/contact/')


