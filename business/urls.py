from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('business.views',
                       (r'^$', 'index'),
                       (r'^setup$', 'setup'),
                       (r'^addSubOrg$', 'add_sub_org'),
                       (r'^subOrganizationForm', 'subOrganizationForm')
                       )
