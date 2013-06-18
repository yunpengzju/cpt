# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.conf import global_settings  
from django.contrib import auth
from django.contrib.auth.decorators import permission_required
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

@permission_required('recruit.go_anywhere', login_url="/login/")
def index(request):
    return render_to_response('recruit/index.html',context_instance=RequestContext(request))
