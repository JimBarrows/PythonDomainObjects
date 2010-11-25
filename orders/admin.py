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

class OrderTermInLine(admin.TabularInline):
	model = OrderTerm
	extra=1

class OrderStatusInLine(admin.TabularInline):
	model = OrderStatus
	extra=1

class PurchaseOrderAdmin( admin.ModelAdmin):
	inlines=[PurchaseOrderItemInLine, OrderRoleInLine, OrderAdjustmentInLine, OrderTermInLine, OrderStatusInLine]

class SalesOrderAdmin( admin.ModelAdmin):
	inlines=[SalesOrderItemInLine, OrderRoleInLine, OrderAdjustmentInLine, OrderTermInLine, OrderStatusInLine]

admin.site.register( PurchaseOrder, PurchaseOrderAdmin )
admin.site.register( SalesOrder, SalesOrderAdmin )
admin.site.register( OrderRole )
admin.site.register( OrderRoleType )
admin.site.register( OrderAdjustmentType )
admin.site.register( SalesTaxLookup )
admin.site.register( OrderTermType )
admin.site.register( OrderStatusType )
