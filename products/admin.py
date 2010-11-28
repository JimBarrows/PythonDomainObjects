from django.contrib import admin
from products.models import *

class CategoryInLine(admin.TabularInline):
	model=Category
	extra=1

class IdentificationInLine(admin.TabularInline):
	model=Identification
	extra=1

class MarketInterestInLine(admin.TabularInline):
	model=MarketInterest
	extra=1

class FeatureInteractionOfInLine(admin.TabularInline):
	model=FeatureInteraction
	fk_name='of'
	extra=1

class FeatureInteractionFactorInInLine(admin.TabularInline):
	model=FeatureInteraction
	fk_name='factor_in'
	extra=1

class FeatureApplicabilityInLine(admin.TabularInline):
	model=FeatureApplicability
	extra=1

class CategoryClassificationInLine(admin.TabularInline):
	model=CategoryClassification
	extra=1

class UnitOfMeasureConversionInLine(admin.TabularInline):
	model=UnitOfMeasureConversion
	extra=1
	fk_name='convert_from'

class SupplierProductInLine(admin.TabularInline):
	model=SupplierProduct
	extra=1

class ReorderGuidelineInLine(admin.TabularInline):
	model=ReorderGuideline
	extra=1

class InventoryItemVarianceInLine(admin.TabularInline):
	model=InventoryItemVariance
	extra=1

class BasePriceInLine(admin.TabularInline):
	model=BasePrice
	extra=1

class DiscountComponentInLine(admin.TabularInline):
	model=DiscountComponent
	extra=1

class SurchargeComponentInLine(admin.TabularInline):
	model=SurchargeComponent
	extra=1

class ManufacturerSuggestedPriceInLine(admin.TabularInline):
	model=ManufacturerSuggestedPrice
	extra=1

class OneTimeChargeInLine(admin.TabularInline):
	model=OneTimeCharge
	extra=1

class RecurringChargeInLine(admin.TabularInline):
	model=RecurringCharge
	extra=1

class UtilizationChargeInLine(admin.TabularInline):
	model=UtilizationCharge
	extra=1

class ServiceAdmin( admin.ModelAdmin):
	inlines=[ CategoryClassificationInLine, FeatureApplicabilityInLine, SupplierProductInLine, BasePriceInLine, 
			DiscountComponentInLine,SurchargeComponentInLine, ManufacturerSuggestedPriceInLine, OneTimeChargeInLine, 
			RecurringChargeInLine, UtilizationChargeInLine ]

class GoodAdmin( admin.ModelAdmin):
	inlines=[ CategoryClassificationInLine, IdentificationInLine, FeatureApplicabilityInLine, SupplierProductInLine, 
			ReorderGuidelineInLine, BasePriceInLine, DiscountComponentInLine, SurchargeComponentInLine,
			ManufacturerSuggestedPriceInLine, OneTimeChargeInLine, OneTimeChargeInLine, RecurringChargeInLine, UtilizationChargeInLine ]

class CategoryAdmin( admin.ModelAdmin):
	inlines=[ MarketInterestInLine, CategoryInLine]

class FeatureAdmin( admin.ModelAdmin):
	inlines=[ FeatureInteractionOfInLine, FeatureInteractionFactorInInLine]

class UnitOfMeasureAdmin( admin.ModelAdmin):
	inlines=[ UnitOfMeasureConversionInLine ]

class InventoryItemAdmin( admin.ModelAdmin):
	inlines=[ InventoryItemVarianceInLine ]

class PartAdmin( admin.ModelAdmin):
	inlines=[ ReorderGuidelineInLine, SupplierProductInLine  ]

admin.site.register( Service, ServiceAdmin)
admin.site.register( Good, GoodAdmin )
admin.site.register( Category, CategoryAdmin )
admin.site.register( Feature,  FeatureAdmin)
admin.site.register( IdentificationType )
admin.site.register( FeatureCategory )
admin.site.register( FeatureInteraction )
admin.site.register( Dimension )
admin.site.register( UnitOfMeasure, UnitOfMeasureAdmin )
admin.site.register( UnitOfMeasureConversion )
admin.site.register( SerializedInventoryItem, InventoryItemAdmin )
admin.site.register( NonSerializedInventoryItem, InventoryItemAdmin )
admin.site.register( Reason )
admin.site.register( ContainerType )
admin.site.register( Container )
admin.site.register( Lot )
admin.site.register( InventoryItemStatusType )
admin.site.register( BasePrice )
admin.site.register( DiscountComponent )
admin.site.register( SurchargeComponent )
admin.site.register( ManufacturerSuggestedPrice )
admin.site.register( OneTimeCharge )
admin.site.register( RecurringCharge )
admin.site.register( UtilizationCharge )
admin.site.register( QuantityBreak )
admin.site.register( OrderValue )
admin.site.register( SaleType )
admin.site.register( TimeFrequencyMeasure )
admin.site.register( CurrencyMeasure )
admin.site.register( EstimatedProductCost )
admin.site.register( CostComponentType )
admin.site.register( ProductAssociation )
admin.site.register( ProductAssociationType )
admin.site.register( FinishedGood, PartAdmin )
admin.site.register( SubAssembly, PartAdmin )
admin.site.register( RawMaterial, PartAdmin )
admin.site.register( PartBom )
