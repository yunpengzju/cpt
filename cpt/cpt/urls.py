from django.conf.urls import patterns, include, url

from cpt import views
from cpt import settings
from recruit.views import index
from contact.views import contact_list, contact_one, contact_me, contact_edit, contact_email

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
    url(r'^join/$', index),
    url(r'^login/$',  login),
    url(r'^logout/$', views.logout_view),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    # contact
    url(r'^contact/$', contact_list),
    url(r'^contact/me/$', contact_me),
    url(r'^contact/edit/$', contact_edit),
    url(r'^contact/(\d+)/$', contact_one),
    url(r'^contact/(\d+)/email/$', contact_email),
)
