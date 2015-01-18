# Create your views here.
from django.http import HttpResponseRedirect
from cpt.statistic.models import Statistic

def enter(request):
    try:
        inst = Statistic.objects.get(id=1)
    except Statistic.DoesNotExist:
        new_statistic = Statistic(1)
        new_statistic.save()
    else:
        inst.site_views += 1
        inst.save()
        return HttpResponseRedirect('/index/')