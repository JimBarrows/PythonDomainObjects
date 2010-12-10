from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from products.models import Product, Feature
from party.models import Party, ContactMechanism

class Invoice( PolymorphicModel ):
	invoice_date = models.DateField()
	message = models.TextField()
	description = models.TextField()
	parties = models.ManyToManyField( Party, through='Role', blank=True, null=True)
	billedTo = models.ForeignKey( Party, related_name="billedTo_set" )
	billedFrom = models.ForeignKey( Party, related_name="billedFrom_set" )
	addressedTo = models.ForeignKey( ContactMechanism, related_name="addressedTo_set" )
	addressedFrom = models.ForeignKey( ContactMechanism, related_name="addressedFrom_set" )

class SalesInvoice( Invoice ):
	pass

class PurchaseInvoice( Invoice ):
	pass

class Item( PolymorphicModel ):
	taxable = models.BooleanField()
	quantity = models.IntegerField()
	description = models.TextField()
	amount = models.DecimalField( max_digits = 8, decimal_places=2)

class AcquiringItem( Item):
	invoice = models.ForeignKey( Invoice )

class ProductItem( Item):
	product = models.ForeignKey( Product,  blank=True, null=True)
	invoice = models.ForeignKey( Invoice )

class FeatureItem( Item):
	feature = models.ForeignKey( Feature, blank=True, null=True )
	invoiceProductItem = models.ForeignKey( ProductItem, blank=True, null=True )
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
	roleType = models.ForeignKey( RoleType)
	percentage = models.DecimalField( max_digits=5, decimal_places=2)
	at = models.DateTimeField(auto_now=True, auto_now_add=True)

