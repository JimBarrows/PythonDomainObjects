from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import index
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import admin
import os.path
WEB_ROOT = os.path.join( os.path.dirname( __file__), '/web')
admin.autodiscover()
urlpatterns = patterns('',
    (r'^business/', include( 'business.urls')),
    (r'^products/', include( 'products.urls')),
		(r'css/(?P<path>.*)$', 'django.views.static.serve', 
				{'document_root': os.path.join( WEB_ROOT, '/static/css/')}),
		(r'img/(?P<path>.*)$', 'django.views.static.serve', 
				{'document_root': '/home/jimbarrows/Desktop/projects/bizondemand-python/web/static/img/'}),
		(r'js/(?P<path>.*)$', 'django.views.static.serve', 
				{'document_root': '/home/jimbarrows/Desktop/projects/bizondemand-python/web/static/js/'}),
    (r'^$', index),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
		(r'^accounts/login/$', 'django.contrib.auth.views.login'),
		(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
)
