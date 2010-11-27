from django.conf.urls.defaults import *
from products.models import Product
from products.forms import GoodForm

products_list = {
	'queryset' : Product.objects.all(),
}

urlpatterns = patterns('',
	(r'^$', 'django.views.generic.list_detail.object_list', products_list),
	(r'^goods/add$', 'django.views.generic.create_update.create_object', { 'form_class': GoodForm}),
)
