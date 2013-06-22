from django.conf.urls import patterns, include, url

from cpt import views
from cpt import settings
from recruit.views import recruit_index,recruit_add_info,recruit_edit
from contact.views import contact_list, contact_one, contact_me, contact_edit
from task.views import task_list, task_new, task_one, task_edit, task_manage

from django.contrib.auth.views import login, logout
# Uncomment the next two lines to enable the admin:
from django.contrib import admin


admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cpt.views.home', name='home'),
    # url(r'^cpt/', include('cpt.foo.urls')),
    url(r'^index/$',views.index),
    url(r'^site_media/(?P<path>.*)$','django.views.static.serve',{'document_root':settings.STATIC_ROOT}), 
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^register/$', views.register),
    url(r'^login/$',  login),
    url(r'^logout/$', views.logout_view),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # contact
    url(r'^contact/$', contact_list),
    url(r'^contact/me/$', contact_me),
    url(r'^contact/edit/$', contact_edit),
    url(r'^contact/(\d+)/$', contact_one),
    #url(r'^contact/(\d+)/email/$', contact_email),
    # recruit
    url(r'^join/$', recruit_index),
    url(r'^join/apply/$',recruit_add_info),
    url(r'^join/edit/$' ,recruit_edit),
    # task
    url(r'^task/$', task_list),
    url(r'^task/new/$', task_new),
    url(r'^task/(\d+)/$', task_one),
    url(r'^task/(\d+)/edit/$', task_edit),
    url(r'^task/(\d+)/manage/$', task_manage),
)
