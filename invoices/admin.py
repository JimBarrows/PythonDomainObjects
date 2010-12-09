from django.contrib import admin
from invoices.models import *

class InvoiceItemInLine( admin.TabularInline):
	model=InvoiceItem
	extra=1

class InvoiceAdmin( admin.ModelAdmin ):
	inlines=[InvoiceItemInLine]

admin.site.register(  InvoiceItemType)
admin.site.register(  Invoice, InvoiceAdmin)
