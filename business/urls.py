from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from views import *


urlpatterns = patterns('business.views',
                       (r'^setup$', BusinessCreate.as_view()),
                       )
