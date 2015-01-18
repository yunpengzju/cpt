from django.conf.urls import patterns, include, url

from cpt.cpt import views
from cpt.cpt import settings
from cpt.recruit.views import recruit_index, recruit_add_info, recruit_edit
from cpt.recruit.views import recruit_admin, recruit_admin_info, recruit_admin_exam, recruit_admin_interview, \
    recruit_admin_presentation
from cpt.contact.views import contact_list, contact_one, contact_me, contact_edit
from cpt.task.views import task_list, task_new, task_one, task_edit
from cpt.task.views import task_operation, task_close, task_del_jj, task_del_xt
from cpt.task.views import task_jj, task_xt, task_contacted, task_cancel, task_success

from cpt.statistic.views import enter
from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       # url(r'^$', 'cpt.views.home', name='home'),
                       # url(r'^cpt/', include('cpt.foo.urls')),
                       url(r'^$', enter),
                       url(r'^index/$', views.index),
                       url(r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
                           {'document_root': settings.STATIC_ROOT}),
                       # Uncomment the admin/doc line below to enable admin documentation:
                       # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^register/$', views.register),
                       url(r'^login/$', login),
                       url(r'^logout/$', views.logout_view),
                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),
                       # contact
                       url(r'^contact/$', contact_list),
                       url(r'^contact/me/$', contact_me),
                       url(r'^contact/edit/$', contact_edit),
                       url(r'^contact/(\d+)/$', contact_one),
                       # url(r'^contact/(\d+)/email/$', contact_email),
                       # recruit
                       url(r'^join/$', recruit_index),
                       url(r'^join/apply/$', recruit_add_info),
                       url(r'^join/edit/$', recruit_edit),
                       url(r'^join/admin/$', recruit_admin),
                       url(r'^join/admin/info/$', recruit_admin_info),
                       url(r'^join/admin/exam/$', recruit_admin_exam),
                       url(r'^join/admin/interview/$', recruit_admin_interview),
                       url(r'^join/admin/presentation/$', recruit_admin_presentation),
                       # task
                       url(r'^task/$', task_list),
                       url(r'^task/new/$', task_new),
                       url(r'^task/(\d+)/$', task_one),
                       url(r'^task/(\d+)/edit/$', task_edit),
                       url(r'^task/(\d+)/operation/$', task_operation),
                       url(r'^task/(\d+)/close/$', task_close),
                       url(r'^task/(\d+)/del-jj/(\d+)/$', task_del_jj),
                       url(r'^task/(\d+)/del-xt/(\d+)/$', task_del_xt),
                       url(r'^task/(\d+)/jj/$', task_jj),
                       url(r'^task/(\d+)/xt/$', task_xt),
                       url(r'^task/(\d+)/contacted/$', task_contacted),
                       url(r'^task/(\d+)/cancel/$', task_cancel),
                       url(r'^task/(\d+)/success/$', task_success),
)
