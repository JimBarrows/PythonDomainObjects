from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from products.models import Product, Feature

class Invoice( models.Model ):
	invoice_date = models.DateField()
	message = models.TextField()
	description = models.TextField()

class InvoiceItem( models.Model ):
	taxable = models.BooleanField()
	quantity = models.IntegerField()
	amount = models.DecimalField( max_digits = 8, decimal_places=2)
	description = models.TextField()
	invoice = models.ForeignKey( Invoice)
	kind = models.ForeignKey( 'InvoiceItemType', blank=True, null=True)
	product = models.ForeignKey( Product,  blank=True, null=True)
	productFeature = models.ForeignKey( Feature, blank=True, null=True )

class InvoiceItemType( models.Model ):
	description = models.CharField( max_length=250 )


