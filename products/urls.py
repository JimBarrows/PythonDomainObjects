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
	(r'^services/add$', login_required(ProductCreate.as_view(model=Service, form_class=ServiceForm, success_url='/products/services'))),
	(r'^services/(?P<pk>\d+)/$',  login_required(ProductDetail.as_view(model=Service))),
	(r'^services/update/(?P<pk>\d+)/$',  login_required(ProductUpdate.as_view(model=Service, form_class=ServiceForm, success_url='/products/services'))),
	(r'^services/delete/(?P<pk>\d+)/$',  login_required(ProductDelete.as_view(model=Service, success_url='/products/services'))),
	(r'^goods$', login_required(ProductsList.as_view( model=Good, queryset = goods_query))),
	(r'^goods/add$', login_required(GoodCreate.as_view(model=Good, form_class=GoodForm, success_url='/products/goods'))),
	(r'^goods/(?P<pk>\d+)/$',  login_required(GoodDetail.as_view(model=Good))),
	(r'^goods/update/(?P<pk>\d+)/$',  login_required(GoodUpdate.as_view(model=Good, form_class=GoodForm, success_url='/products/goods'))),
	(r'^goods/delete/(?P<pk>\d+)/$',  login_required(ProductDelete.as_view(model=Good, success_url='/products/goods'))),
	(r'^classifications$', login_required(CategoryList.as_view( ))),
	(r'^classifications/add$', login_required(CategoryCreate.as_view( ))),
	(r'^classifications/(?P<pk>\d+)/$', login_required(CategoryDetail.as_view( ))),
	(r'^classifications/update/(?P<pk>\d+)/$', login_required(CategoryUpdate.as_view( ))),
	(r'^classifications/delete/(?P<pk>\d+)/$',  login_required(CategoryDelete.as_view())),
	(r'^pricing/base_prices$', login_required(BasePriceList.as_view( ))),
	(r'^pricing/base_prices/add$', login_required(BasePriceCreate.as_view( ))),
	(r'^pricing/base_prices/(?P<pk>\d+)/$', login_required(BasePriceDetail.as_view( ))),
	(r'^pricing/base_prices/update/(?P<pk>\d+)/$', login_required(BasePriceUpdate.as_view( ))),
	(r'^pricing/base_prices/delete/(?P<pk>\d+)/$', login_required(BasePriceDelete.as_view( ))),
	(r'^pricing/discounts$', login_required(DiscountComponentList.as_view( ))),
	(r'^pricing/discounts/add$', login_required(DiscountComponentCreate.as_view( ))),
	(r'^pricing/discounts/(?P<pk>\d+)/$', login_required(DiscountComponentDetail.as_view( ))),
	(r'^pricing/discounts/update/(?P<pk>\d+)/$', login_required(DiscountComponentUpdate.as_view( ))),
	(r'^pricing/discounts/delete/(?P<pk>\d+)/$', login_required(DiscountComponentDelete.as_view( ))),
	(r'^pricing/surcharges$', login_required(SurchargeComponentList.as_view( ))),
	(r'^pricing/surcharges/add$', login_required(SurchargeComponentCreate.as_view( ))),
	(r'^pricing/surcharges/(?P<pk>\d+)/$', login_required(SurchargeComponentDetail.as_view( ))),
	(r'^pricing/surcharges/update/(?P<pk>\d+)/$', login_required(SurchargeComponentUpdate.as_view( ))),
	(r'^pricing/surcharges/delete/(?P<pk>\d+)/$', login_required(SurchargeComponentDelete.as_view( ))),
	(r'^pricing/msrps$', login_required(ManufacturersSuggestedRetailPriceList.as_view( ))),
	(r'^pricing/msrps/add$', login_required(ManufacturersSuggestedRetailPriceCreate.as_view( ))),
	(r'^pricing/msrps/(?P<pk>\d+)/$', login_required(ManufacturersSuggestedRetailPriceDetail.as_view( ))),
	(r'^pricing/msrps/update/(?P<pk>\d+)/$', login_required(ManufacturersSuggestedRetailPriceUpdate.as_view( ))),
	(r'^pricing/msrps/delete/(?P<pk>\d+)/$', login_required(ManufacturersSuggestedRetailPriceDelete.as_view( ))),
	(r'^costing$', login_required(EstimatedProductCostList.as_view( ))),
	(r'^costing/add$', login_required(EstimatedProductCostCreate.as_view( ))),
	(r'^costing/(?P<pk>\d+)/$', login_required(EstimatedProductCostDetail.as_view( ))),
	(r'^costing/update/(?P<pk>\d+)/$', login_required(EstimatedProductCostUpdate.as_view( ))),
	(r'^costing/delete/(?P<pk>\d+)/$', login_required(EstimatedProductCostDelete.as_view( ))),
	(r'^features$', login_required(FeatureList.as_view( ))),
	(r'^features/add$', login_required(FeatureCreate.as_view( ))),
	(r'^features/(?P<pk>\d+)/$', login_required(FeatureDetail.as_view( ))),
	(r'^features/update/(?P<pk>\d+)/$', login_required(FeatureUpdate.as_view( ))),
	(r'^features/delete/(?P<pk>\d+)/$', login_required(FeatureDelete.as_view( ))),
	(r'^features/product_quality$', login_required(ProductQualityList.as_view( ))),
	(r'^features/product_quality/add$', login_required(ProductQualityCreate.as_view( ))),
	(r'^features/product_quality/(?P<pk>\d+)$', login_required(ProductQualityDetail.as_view( ))),
	(r'^features/product_quality/update/(?P<pk>\d+)$', login_required(ProductQualityUpdate.as_view( ))),
	(r'^features/product_quality/delete/(?P<pk>\d+)$', login_required(ProductQualityDelete.as_view( ))),
)
