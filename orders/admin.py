from django.contrib import admin
from orders.models import *

class PurchaseOrderItemInLine(admin.TabularInline):
	model=PurchaseOrderItem
	extra=1

class SalesOrderItemInLine(admin.TabularInline):
	model = SalesOrderItem
	extra=1

class PurchaseOrderAdmin( admin.ModelAdmin):
	inlines=[PurchaseOrderItemInLine]

class SalesOrderAdmin( admin.ModelAdmin):
	inlines=[SalesOrderItemInLine]

admin.site.register( PurchaseOrder, PurchaseOrderAdmin )
admin.site.register( SalesOrder, SalesOrderAdmin )
