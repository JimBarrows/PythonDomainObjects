from django.conf.urls import patterns, include, url
from views import index
from django.contrib import admin
import os.path
WEB_ROOT = os.path.join(os.path.dirname(__file__), '/web')
admin.autodiscover()
urlpatterns = patterns('',
                       url (r'^business/', include('business.urls')),
                       url(r'^crm/', include('crm.urls')),
                       url(r'^orders/', include('orders.urls')),
                       url(r'^products/', include('products.urls')),
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^accounts/login/$', 'django.contrib.auth.views.login'),
                       url(r'^accounts/logout/$', 'django.contrib.auth.views.logout'),
                       url(r'^$', index),
                       )
