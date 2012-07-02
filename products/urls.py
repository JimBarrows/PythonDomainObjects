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
	(r'^categories$', login_required(CategoryList.as_view( ))),
	(r'^categories/add$', login_required(CategoryCreate.as_view( ))),
	(r'^categories/(?P<pk>\d+)/$', login_required(CategoryDetail.as_view( ))),
	(r'^categories/update/(?P<pk>\d+)/$', login_required(CategoryUpdate.as_view( ))),
	(r'^categories/delete/(?P<pk>\d+)/$',  login_required(CategoryDelete.as_view())),
	(r'^pricing$', login_required(PricingComponentList.as_view( ))),
	(r'^pricing/add$', login_required(PricingComponentCreate.as_view( ))),
	(r'^pricing/(?P<pk>\d+)/$', login_required(PricingComponentDetail.as_view( ))),
	(r'^pricing/update/(?P<pk>\d+)/$', login_required(PricingComponentUpdate.as_view( ))),
	(r'^pricing/delete/(?P<pk>\d+)/$', login_required(PricingComponentDelete.as_view( ))),
	(r'^costing$', login_required(EstimatedProductCostList.as_view( ))),
	(r'^costing/add$', login_required(EstimatedProductCostCreate.as_view( ))),
	(r'^costing/(?P<pk>\d+)/$', login_required(EstimatedProductCostDetail.as_view( ))),
	(r'^costing/update/(?P<pk>\d+)/$', login_required(EstimatedProductCostUpdate.as_view( ))),
	(r'^costing/delete/(?P<pk>\d+)/$', login_required(EstimatedProductCostDelete.as_view( ))),
)
