from django.conf.urls import patterns, url
from views import BusinessCreate


urlpatterns = patterns('business.views',
                       url(r'^setup$', BusinessCreate.as_view()),
                       )
