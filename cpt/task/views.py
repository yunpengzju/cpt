# coding=utf-8
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
    result = Task.objects.order_by("-date") # 按时间倒序
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

        # 发布者在状态0下有权限
        if visitor.number != inst.post_id or inst.state != 0:
            return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
        
        if request.method == 'POST':
            form = TaskForm(request.POST, instance = inst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/task/'+str(task_id)+'/')
        else:
            form = TaskForm(instance = inst);
        return render_to_response('task/edit.html', locals(), context_instance=RequestContext(request))
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_member', login_url="/login/")
def task_operation(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        
        xietiao = Xietiao.objects.filter(task = task_id)
        for item in xietiao:
            try:
                item.name = Contact.objects.get(number = item.member).name
            except Contact.DoesNotExist:
                del item

        jiangjie = Jiangjie.objects.filter(task = task_id)
        for item in jiangjie:
            try:
                item.name = Contact.objects.get(number = item.member).name
            except Contact.DoesNotExist:
                del item
    
        return render_to_response('task/operation.html', locals(), context_instance=RequestContext(request))
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_manage', login_url="/task/")
def task_close(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        # 管理者在状态0下有权限
        if task.state == 0:
            task.state = 1;
            task.save()
        return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_manage', login_url="/task/")
def task_del_jj(request, task_id, member_id):
    Jiangjie.objects.filter(task=task_id, member=member_id).delete()
    return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')

@permission_required('task.is_manage', login_url="/task/")
def task_del_xt(request, task_id, member_id):
    Xietiao.objects.filter(task=task_id, member=member_id).delete()
    return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')

@permission_required('task.is_member', login_url="/login/")
def task_jj(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        visitor = Contact.objects.get(nickname = request.user.username)
        # 队员在状态0下有权限
        if task.state == 0:
            Jiangjie.objects.create(
                task = task_id,
                member = visitor.number
            )
        return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_member', login_url="/login/")
def task_xt(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        visitor = Contact.objects.get(nickname = request.user.username)
        # 队员在状态0下有权限
        if task.state == 0:
            Xietiao.objects.create(
                task = task_id,
                member = visitor.number
            )
        return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')
    return

@permission_required('task.is_member', login_url="/login/")
def task_contacted(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        member = Contact.objects.get(nickname=request.user.username)
        jj = Jiangjie.objects.filter(task=task_id, member=member.number).count()
        xt = Xietiao.objects.filter(task=task_id, member=member.number).count()
        # 协调员或讲解员在状态1下有权限
        if (jj != 0 or xt != 0) and task.state == 1:
            print "why here"
            task.state = 2;
            task.save()
        return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_member', login_url="/login/")
def task_cancel(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        member = Contact.objects.get(nickname=request.user.username)
        jj = Jiangjie.objects.filter(task=task_id, member=member.number).count()
        xt = Xietiao.objects.filter(task=task_id, member=member.number).count()
        # 协调员或讲解员在状态2下有权限
        if (jj != 0 or xt != 0) and task.state == 2:
            print "why here"
            task.state = 4;
            task.save()
        return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')

@permission_required('task.is_member', login_url="/login/")
def task_success(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
        member = Contact.objects.get(nickname=request.user.username)
        jj = Jiangjie.objects.filter(task=task_id, member=member.number).count()
        xt = Xietiao.objects.filter(task=task_id, member=member.number).count()
        # 协调员或讲解员在状态2下有权限
        if (jj != 0 or xt != 0) and task.state == 2:
            print "why here"
            task.state = 3;
            task.save()
        return HttpResponseRedirect('/task/'+str(task_id)+'/operation/')
    except Task.DoesNotExist:
        return HttpResponseRedirect('/task/')
    except Contact.DoesNotExist:
        return HttpResponseRedirect('/task/')


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

