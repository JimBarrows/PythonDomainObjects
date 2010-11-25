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

class PurchaseOrderAdmin( admin.ModelAdmin):
	inlines=[PurchaseOrderItemInLine, OrderRoleInLine]

class SalesOrderAdmin( admin.ModelAdmin):
	inlines=[SalesOrderItemInLine, OrderRoleInLine]

admin.site.register( PurchaseOrder, PurchaseOrderAdmin )
admin.site.register( SalesOrder, SalesOrderAdmin )
admin.site.register( OrderRole )
admin.site.register( OrderRoleType )
