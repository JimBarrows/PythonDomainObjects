from django.conf.urls.defaults import *

urlpatterns = patterns('products.views',
	(r'^$', 'index'),
	(r'^goods$',  'good_index'),
	(r'^goods/(?P<good_id>\d+)/$',  'good_edit'),
	(r'^goods/add$',  'good_add'),
	(r'^goods/save$',  'good_save'),
	(r'^goods/(?P<good_id>\d+)/save$',  'good_update'),
)
