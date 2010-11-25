from django.contrib import admin
from orders.models import *

class PurchaseOrderItemInLine(admin.TabularInline):
	model=PurchaseOrderItem
	extra=1

class SalesOrderItemInLine(admin.TabularInline):
	model = SalesOrderItem
	extra=1

class OrderRoleInLine(admin.TabularInline):
	model = OrderRole
	extra=1

class OrderAdjustmentInLine(admin.TabularInline):
	model = OrderAdjustment
	extra=1

class PurchaseOrderAdmin( admin.ModelAdmin):
	inlines=[PurchaseOrderItemInLine, OrderRoleInLine, OrderAdjustmentInLine]

class SalesOrderAdmin( admin.ModelAdmin):
	inlines=[SalesOrderItemInLine, OrderRoleInLine, OrderAdjustmentInLine]

admin.site.register( PurchaseOrder, PurchaseOrderAdmin )
admin.site.register( SalesOrder, SalesOrderAdmin )
admin.site.register( OrderRole )
admin.site.register( OrderRoleType )
admin.site.register( OrderAdjustmentType )
admin.site.register( SalesTaxLookup )
