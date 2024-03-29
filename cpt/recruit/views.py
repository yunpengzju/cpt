# coding=utf-8
# Create your views here.
import string

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import global_settings
from django.contrib import auth
from django.contrib.auth.decorators import permission_required, login_required

TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

from cpt.recruit.models import Candidate
from cpt.recruit.models import CandidateForm, Exam, Exam_list, Interview, Interview_list, Presentation, \
    Presentation_list


@login_required(login_url="/login/")
def recruit_index(request):
    try:
        inst = Candidate.objects.get(user_name=request.user.username)
        is_exist = True
        if inst.state == 0:
            return render_to_response('recruit/state0.html', locals(), context_instance=RequestContext(request))
        if inst.state == 1:
            if request.method == 'POST':  # remember to check the max_num
                exam = Exam.objects.get(id=request.POST.get('selection'))
                if exam.max_num > 0:
                    exam.max_num = exam.max_num - 1
                    exam.save()
                    p = Candidate.objects.get(user_name=request.user.username)
                    inst = Exam_list(user_name=p.real_name, user_id=p.id, exam_id=request.POST.get('selection'))
                    inst.save()
                    p.state = 2
                    p.save()
                    return HttpResponseRedirect('/join/')
                else:
                    message = "该考场已满，如无合适考场请联系负责人……"
                    list = Exam.objects.all()
                    return render_to_response('recruit/state1.html', locals(), context_instance=RequestContext(request))
            else:
                list = Exam.objects.all()
                return render_to_response('recruit/state1.html', locals(), context_instance=RequestContext(request))
        if inst.state == 2:
            exam = Exam_list.objects.get(user_id=inst.id)
            eid = exam.exam_id
            exam = Exam.objects.get(id=eid)
            return render_to_response('recruit/state2.html', locals(), context_instance=RequestContext(request))
        if inst.state == 3:
            if request.method == 'POST':  # remember to check the max_num
                inter = Interview.objects.get(id=request.POST.get('selection'))
                if inter.max_num > 0:
                    inter.max_num = inter.max_num - 1
                    inter.save()
                    inter_list = Interview_list(user_name=inst.real_name, user_id=inst.id,
                                                interview_id=request.POST.get('selection'))
                    inter_list.save()
                    inst.state = 4
                    inst.save()
                    return HttpResponseRedirect('/join/')
                else:
                    message = "该场次已满，如无合适场次请联系负责人……"
                    list = Interview.objects.all()
                    return render_to_response('recruit/state3.html', locals(), context_instance=RequestContext(request))
            else:
                list = Interview.objects.all()
                return render_to_response('recruit/state3.html', locals(), context_instance=RequestContext(request))
        if inst.state == 4:
            inter = Interview_list.objects.get(user_id=inst.id)
            iid = inter.interview_id
            interview = Interview.objects.get(id=iid)
            return render_to_response('recruit/state4.html', locals(), context_instance=RequestContext(request))
        if inst.state == 5:
            if request.method == 'POST':  # remember to check the max_num
                inter = Presentation.objects.get(id=request.POST.get('selection'))
                if inter.max_num > 0:
                    inter.max_num = inter.max_num - 1
                    inter.save()
                    inter_list = Presentation_list(user_name=inst.real_name, user_id=inst.id,
                                                   presentation_id=request.POST.get('selection'))
                    inter_list.save()
                    inst.state = 6
                    inst.save()
                    return HttpResponseRedirect('/join/')
                else:
                    message = "该场次已满，如无合适场次请联系负责人……"
                    list = Presentation.objects.all()
                    return render_to_response('recruit/state5.html', locals(), context_instance=RequestContext(request))
            else:
                list = Presentation.objects.all()
                return render_to_response('recruit/state5.html', locals(), context_instance=RequestContext(request))
        if inst.state == 6:
            inter = Presentation_list.objects.get(user_id=inst.id)
            iid = inter.presentation_id
            presentation = Presentation.objects.get(id=iid)
            return render_to_response('recruit/state6.html', locals(), context_instance=RequestContext(request))
        if inst.state == 7:
            return render_to_response('recruit/state7.html', locals(), context_instance=RequestContext(request))
        if inst.state == 8:
            return render_to_response('recruit/state8.html', locals(), context_instance=RequestContext(request))

    except:
        is_exist = False
        return render_to_response('recruit/index.html', locals(), context_instance=RequestContext(request))


@login_required(login_url="/login/")
def recruit_add_info(request):
    if request.method == 'POST':
        inst = Candidate.objects.get(user_name=request.user.username)
        form = CandidateForm(request.POST, instance=inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/join/')
    else:
        p = Candidate(user_name=request.user.username, user_id=request.user.id, state=0)
        p.save()
        inst = Candidate.objects.get(user_name=request.user.username)
        form = CandidateForm(request.POST, instance=inst)
        return render_to_response('recruit/candidate_form.html', locals(), context_instance=RequestContext(request))


@login_required(login_url="/login/")
def recruit_edit(request):
    try:
        inst = Candidate.objects.get(user_name=request.user.username)
        if request.method == 'POST':
            form = CandidateForm(request.POST, instance=inst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/join/')
        else:
            form = CandidateForm(instance=inst)
        return render_to_response('recruit/candidate_form.html', locals(), context_instance=RequestContext(request))
    except Candidate.DoesNotExist:
        return HttpResponseRedirect('/join/')


def recruit_admin(request):
    return render_to_response('recruit/admin.html', locals(), context_instance=RequestContext(request))


def recruit_admin_info(request):
    res = admin_fun(request, 0, 'info')
    return res


def recruit_admin_exam(request):
    res = admin_fun(request, 2, 'exam')
    return res


def recruit_admin_interview(request):
    res = admin_fun(request, 4, 'interview')
    return res


def recruit_admin_presentation(request):
    res = admin_fun(request, 6, 'presentation')
    return res


def admin_fun(request, state, path):
    if request.user.is_superuser:
        if request.method == 'POST':
            accept_list = request.REQUEST.getlist('accept')
            refuse_list = request.REQUEST.getlist('refuse')
            for item in accept_list:
                inst = Candidate.objects.get(user_name=item)
                inst.state = inst.state + 1
                inst.save()
            for item in refuse_list:
                inst1 = Candidate.objects.get(user_name=item)
                inst1.state = 8
                inst1.save()
            return HttpResponseRedirect('/join/admin/exam/')
        else:
            try:
                list = Candidate.objects.all().filter(state__exact=state).order_by('id')
                url = path
            except:
                no_list = True
                message = '没有待选择人选'
            return render_to_response('recruit/admin_form.html', locals(), context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/join/')