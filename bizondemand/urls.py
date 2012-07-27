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
    (r'^crm/', include( 'crm.urls')),
    (r'^orders/', include( 'orders.urls')),
    (r'^products/', include( 'products.urls')),
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^admin/', include(admin.site.urls)),
		(r'^accounts/login/$', 'django.contrib.auth.views.login'),
		(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
    (r'^$', index),
)
