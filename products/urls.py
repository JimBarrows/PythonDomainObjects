from django.conf.urls.defaults import *
from views import *
urlpatterns = patterns('products.views',
#                       (r'^goods$',  good_index),
#                       (r'^goods/(?P<good_id>\d+)/$',  good_edit),
#                       (r'^goods/add$',  good_add),
#                       (r'^goods/save$',  good_save),
#                       (r'^goods/(?P<good_id>\d+)/save$',  good_update),
	(r'^services$', login_required(ServicesList.as_view())),
	(r'^services/add$', login_required(ServicesCreate.as_view())),
#                       (r'^services/(?P<service_id>\d+)/$',  service_edit),
#                       (r'^services/save$',  service_save),
#                       (r'^services/(?P<service_id>\d+)/save$',  service_update),
                       )
