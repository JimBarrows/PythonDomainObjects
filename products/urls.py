from django.conf.urls.defaults import *

urlpatterns = patterns('products.views',
	(r'^$', 'index'),
	(r'^goods/add$',  'good_add'),
	(r'^goods/save$',  'good_save'),
)
