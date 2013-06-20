# coding=utf-8
# Create your views here.
import string

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect
from django.conf import global_settings
from django.contrib import auth
from django.contrib.auth.decorators import permission_required,login_required
TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS

from recruit.models import Candidate
from recruit.models import CandidateForm,Exam,Exam_list

@login_required(login_url="/login/")
def recruit_index(request):
    try:
        inst = Candidate.objects.get(user_name=request.user.username)
        is_exist = True
        if inst.state == 0:
            return render_to_response('recruit/state0.html',locals(),context_instance=RequestContext(request))
        if inst.state == 1:
            if request.method == 'POST':    #remember to check the max_num
                exam = Exam.objects.get(id = request.POST.get('selection'))
                if exam.max_num > 0:
                    exam.max_num = exam.max_num-1
                    exam.save()
                    inst = Exam_list(user_name = request.user.username, exam_id = request.POST.get('selection'))
                    inst.save()
                    p = Candidate.objects.get(user_name=request.user.username)
                    p.state = 2
                    p.save()
                    return HttpResponseRedirect('/join/')
                else:
                    message = "该考场已满，如无合适考场请联系负责人……"
                    list = Exam.objects.all()
                    return render_to_response('recruit/state1.html',locals(),context_instance=RequestContext(request))
            else:
                list = Exam.objects.all()
                return render_to_response('recruit/state1.html',locals(),context_instance=RequestContext(request))
        if inst.state == 2:
            exam = Exam_list.objects.get(user_name=request.user.username)
            eid   = exam.exam_id
            exam = Exam.objects.get(id = eid)
            return render_to_response('recruit/state2.html',locals(),context_instance=RequestContext(request))
    except:
        is_exist = False
        return render_to_response('recruit/index.html',locals(),context_instance=RequestContext(request))

@login_required(login_url="/login/")
def recruit_add_info(request):
    if request.method == 'POST':
        inst = Candidate.objects.get(user_name=request.user.username)
        form = CandidateForm(request.POST,instance = inst)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/join/')
    else:
        p = Candidate(user_name = request.user.username, state = 0)
        p.save()
        inst = Candidate.objects.get(user_name=request.user.username)
        form = CandidateForm(request.POST,instance = inst)
        return render_to_response('recruit/candidate_form.html', locals(),context_instance=RequestContext(request))

@login_required(login_url="/login/")
def recruit_edit(request):
    try:
        inst = Candidate.objects.get(user_name = request.user.username)
        if request.method == 'POST':
            form = CandidateForm(request.POST,instance = inst)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/join/')
        else:
            form = CandidateForm(instance = inst)
        return render_to_response('recruit/candidate_form.html', locals(),context_instance=RequestContext(request))
    except Candidate.DoesNotExist:
        return HttpResponseRedirect('/join/')
