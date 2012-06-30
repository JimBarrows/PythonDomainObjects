from django.conf.urls.defaults import *
from views import *

goods_query = Good.objects.filter( 
		(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
		(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
		)

service_query = Service.objects.filter( 
		(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
		(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
		)

urlpatterns = patterns('products.views',
	(r'^services$', login_required(ProductsList.as_view( model=Service, queryset=service_query))),
	(r'^services/add$', login_required(ProductsCreate.as_view(model=Service, form_class=ServiceForm, success_url='/products/services'))),
	(r'^services/(?P<pk>\d+)/$',  login_required(ProductsDetail.as_view(model=Service))),
	(r'^services/update/(?P<pk>\d+)/$',  login_required(ProductUpdate.as_view(model=Service, form_class=ServiceForm, success_url='/products/services'))),
	(r'^services/delete/(?P<pk>\d+)/$',  login_required(ProductDelete.as_view(model=Service, success_url='/products/services'))),
	(r'^goods$', login_required(ProductsList.as_view( model=Good, queryset = goods_query))),
	(r'^goods/add$', login_required(ProductsCreate.as_view(model=Good, form_class=GoodForm, success_url='/products/goods'))),
	(r'^goods/(?P<pk>\d+)/$',  login_required(ProductsDetail.as_view(model=Good))),
	(r'^goods/update/(?P<pk>\d+)/$',  login_required(ProductUpdate.as_view(model=Good, form_class=GoodForm, success_url='/products/goods'))),
	(r'^goods/delete/(?P<pk>\d+)/$',  login_required(ProductDelete.as_view(model=Good, success_url='/products/goods'))),
                       )
