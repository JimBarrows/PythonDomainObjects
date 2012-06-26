from django.conf.urls.defaults import *
from views import *
urlpatterns = patterns('products.views',
	(r'^services$', login_required(ServicesList.as_view())),
	(r'^services/add$', login_required(ServicesCreate.as_view())),
	(r'^services/(?P<pk>\d+)/$',  login_required(ServicesUpdate.as_view())),
	(r'^services/delete/(?P<pk>\d+)/$',  login_required(ServicesDelete.as_view())),
                       )
