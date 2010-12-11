from django.contrib import admin
from invoices.models import *

class SalesInvoiceItemInLine( admin.TabularInline):
	model=SalesInvoiceItem
	extra=1

class PurchaseInvoiceItemInLine( admin.TabularInline):
	model=PurchaseInvoiceItem
	extra=1

class ProductItemInLine( admin.TabularInline):
	model=ProductItem
	extra=1

class FeatureItemInLine( admin.TabularInline):
	model=FeatureItem
	extra=1

class AdjustmentInLine( admin.TabularInline):
	model=Adjustment
	extra=1

class RoleInLine( admin.TabularInline):
	model=Role
	extra=1

class OrderItemBillingInLine( admin.TabularInline):
	model=OrderItemBilling
	extra=1

class SalesInvoiceAdmin( admin.ModelAdmin ):
	inlines=[SalesInvoiceItemInLine, AdjustmentInLine, ProductItemInLine, FeatureItemInLine, RoleInLine]

class PurchaseInvoiceAdmin( admin.ModelAdmin ):
	inlines=[PurchaseInvoiceItemInLine, AdjustmentInLine, ProductItemInLine, FeatureItemInLine, RoleInLine]

class ItemAdmin( admin.ModelAdmin ):
	inlines=[OrderItemBillingInLine]

admin.site.register(  SalesInvoice, SalesInvoiceAdmin)
admin.site.register(  PurchaseInvoice, PurchaseInvoiceAdmin)
admin.site.register( Item, ItemAdmin)
admin.site.register( AdjustmentType)
admin.site.register( RoleType)
