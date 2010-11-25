from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    (r'^business/', include( 'business.urls')),
		(r'css/(?P<path>.*)$', 'django.views.static.serve', 
				{'document_root': '/home/jimbarrows/Desktop/bizondemand/css/'}),
		(r'img/(?P<path>.*)$', 'django.views.static.serve', 
				{'document_root': '/home/jimbarrows/Desktop/bizondemand/img/'}),
		(r'js/(?P<path>.*)$', 'django.views.static.serve', 
				{'document_root': '/home/jimbarrows/Desktop/bizondemand/js/'}),
    (r'^$', direct_to_template, { 'template':'index.html'}),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
)
