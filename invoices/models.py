from datetime import datetime
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymodels.models import PolymorphicModel
from products.models import Product, Feature
from party.models import Party, ContactMechanism
from orders.models import OrderItem

class Invoice( PolymorphicModel ):
	invoice_date = models.DateField()
	message = models.TextField()
	description = models.TextField()
	parties = models.ManyToManyField( Party, through='Role', blank=True, null=True)
	billed_to = models.ForeignKey( Party, related_name="billedTo_set" )
	billed_from = models.ForeignKey( Party, related_name="billedFrom_set" )
	addressed_to = models.ForeignKey( ContactMechanism, related_name="addressedTo_set" )
	addressed_from = models.ForeignKey( ContactMechanism, related_name="addressedFrom_set" )
	paid_via = models.ManyToManyField( 'Payment', through='PaymentApplication', blank=True, null=True)

class SalesInvoice( Invoice ):
	pass

class PurchaseInvoice( Invoice ):
	pass

class InvoiceItemType ( models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey( 'self', blank=True, null=True, related_name='child_set')
	def __unicode__(self):
		return self.description

class Item( PolymorphicModel ): 
	taxable = models.BooleanField() 
	quantity = models.IntegerField()
	description = models.TextField()
	amount = models.DecimalField( max_digits = 8, decimal_places=2)
	order_items = models.ManyToManyField( OrderItem, through='OrderItemBilling', blank=True, null=True)
	describedBy = models.ForeignKey( InvoiceItemType)

class AcquiringItem( Item):
	invoice = models.ForeignKey( Invoice )

class ProductItem( Item):
	product = models.ForeignKey( Product,  blank=True, null=True)
	invoice = models.ForeignKey( Invoice )

class FeatureItem( Item):
	feature = models.ForeignKey( Feature, blank=True, null=True )
	invoice_product_item = models.ForeignKey( ProductItem, blank=True, null=True )
	invoice = models.ForeignKey( Invoice )

class Adjustment( Item):
	perentage = models.DecimalField( max_digits = 5, decimal_places=2)
	invoice = models.ForeignKey( Invoice )
	kind = models.ForeignKey( 'AdjustmentType')

class AdjustmentType( models.Model):
	description = models.CharField(max_length=250)

class PurchaseInvoiceItem( Item ):
	invoice = models.ForeignKey( PurchaseInvoice )

class SalesInvoiceItem( Item ):
	invoice = models.ForeignKey( SalesInvoice )

class RoleType ( models.Model):
	description = models.CharField(max_length=250)

class Role( models.Model):
	invoice = models.ForeignKey( Invoice)
	party = models.ForeignKey( Party)
	role_type = models.ForeignKey( RoleType)
	percentage = models.DecimalField( max_digits=5, decimal_places=2)
	at = models.DateTimeField(auto_now=True, auto_now_add=True)

class OrderItemBilling( models.Model) :
	invoice_item = models.ForeignKey( Item )
	order_item = models.ForeignKey( OrderItem )
	quantity = models.IntegerField()
	amount = models.DecimalField( max_digits = 9, decimal_places=2)

class TermType ( models.Model):
	description = models.CharField(max_length=250)

class Term( models.Model) :
	value = models.IntegerField()
	kind = models.ForeignKey( TermType )
	item = models.ForeignKey( Item )
	invoice = models.ForeignKey( Invoice )

class StatusType ( models.Model):
	description = models.CharField(max_length=250)

class Status( models.Model) :
	date = models.DateField()
	invoice = models.ForeignKey( Invoice )
	kind = models.ForeignKey( StatusType )

class PaymentMethodType ( models.Model):
	description = models.CharField(max_length=250)

class BillingAccount( models.Model):
	from_date = models.DateField()
	thru_date = models.DateField()
	description = models.CharField(max_length=250)

class Payment( PolymorphicModel):
	effective_date = models.DateField()
	reference_number = models.IntegerField()
	amount = models.DecimalField( max_digits = 9, decimal_places=2)
	comment = models.TextField()
	paid_via = models.ForeignKey( PaymentMethodType )
	paid_from = models.ForeignKey( Party, related_name="paidFrom_set" )
	paid_to = models.ForeignKey( Party, related_name="paidTo_set" )

class Receipt( Payment ) :
	deposit = models.ForeignKey( 'Deposit' )

class Disbursement( Payment ) :
	pass


class PaymentApplication( models.Model) :
	invoice = models.ForeignKey( Invoice )
	payment = models.ForeignKey( Payment )
	applied_to = models.ForeignKey( BillingAccount )
	amount_applied = models.DecimalField( max_digits = 9, decimal_places=2)

class FinancialAccountRoleType( models.Model):
	description = models.CharField(max_length=250)

class FinancialAccountRole( models.Model):
	kind = models.ForeignKey( FinancialAccountRoleType)
	from_date = models.DateField( default=datetime.today())
	thru_date = models.DateField( blank=True, null=True)
	party = models.ForeignKey( Party)
	account = models.ForeignKey( 'FinancialAccount')

class FinancialAccountType( models.Model):
	description = models.CharField(max_length=250)

class FinancialAccount( models.Model):
	name = models.CharField( max_length = 250 )
	kind = models.ForeignKey( FinancialAccountType)
	owned_by = models.ManyToManyField( Party, through='FinancialAccountRole', blank=True, null=True)

class FinancialAccountTransaction( PolymorphicModel):
	transaction_date = models.DateField();
	entry_date = models.DateField();
	account = models.ForeignKey( FinancialAccount)
	party = models.ForeignKey( Party)

class Withdrawal ( FinancialAccountTransaction):
	disbursement = models.OneToOneField( Disbursement )

class Deposit ( FinancialAccountTransaction):
	pass

class FinancialAccountAdjustment ( FinancialAccountTransaction):
	pass
