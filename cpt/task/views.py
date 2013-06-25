from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.conf import global_settings
from django.contrib import auth
from django.contrib.auth.decorators import permission_required

from task.models import Task, Xietiao, Jiangjie
from task.models import TaskForm
from contact.models import Contact

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

@permission_required('task.is_member', login_url="/login/")
def task_list(request):
    result = Task.objects.order_by("-date")
    return render_to_response('task/list.html', locals(), context_instance=RequestContext(request))

@permission_required('task.is_member', login_url="/login/")
def task_new(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            try:
                db_new_task(form.cleaned_data, request.user.username)
                return HttpResponseRedirect('/task/')
            except Task.DoesNotExist:
                return render_to_response('task/new.html', locals(), context_instance=RequestContext(request))
    else:
        form = TaskForm()
    return render_to_response('task/new.html', locals(), context_instance=RequestContext(request))

@permission_required('task.is_member', login_url="/login/")
def task_one(request, task_id):
    try:
        result = Task.objects.get(id=task_id);
        return render_to_response('task/one.html', locals(), context_instance=RequestContext(request))
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_member', login_url="/login/")
def task_edit(request, task_id):
    try:
        inst = Task.objects.get(id=task_id)

        visitor = Contact.objects.get(nickname = request.user.username)
        if visitor.number != inst.post_id or inst.state != 0:
            return HttpResponseRedirect('/task/'+str(task_id)+'/')
        
        if request.method == 'POST':
            form = TaskForm(request.POST, instance = inst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/task/')
        else:
            form = TaskForm(instance = inst);
        return render_to_response('task/edit.html', locals(), context_instance=RequestContext(request))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')


@permission_required('task.is_manage', login_url="/task/")
def task_manage(request, task_id):
    return

def db_new_task(formdata, post_nickname):
    post_info = Contact.objects.get(nickname = post_nickname)
    
    Task.objects.create(
        title       = formdata['title'],
        date        = formdata['date'],
        time        = formdata['time'],
        client      = formdata['client'],
        client_num  = formdata['client_num'],
        content     = formdata['content'],
        source      = formdata['source'],
        contact_man = formdata['contact_man'],
        contact_way = formdata['contact_way'],
        post_id     = post_info.number,
        post_man    = post_info.name,
        #post_date   = 
        priority    = formdata['priority'],
        formal      = formdata['formal'],
        note        = formdata['note'],
        expect_xietiao  = formdata['expect_xietiao'],
        expect_jiangjie = formdata['expect_jiangjie'],
        state       = 0
    )
    return

