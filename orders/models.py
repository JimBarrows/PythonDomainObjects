from django.db import models
from polymorphic import PolymorphicModel
from party.models import PartyRoleType
from products.models import Product, Feature

class Order( PolymorphicModel ):
	orderDate = models.DateField()
	entryDate = models.DateField()

class PurchaseOrder( Order):
	''' Purchase Order '''

class SalesOrder( Order):
	''' Sales Order '''

class OrderItem( models.Model ):
	quantity = models.IntegerField(),
	unitPrice = models.DecimalField( max_digits=8, decimal_places=2)
	estimatedDeliveryDate = models.DateField()
	shippingInstructions = models.TextField()
	itemDescription = models.TextField()
	comment = models.TextField()
	orderedWith = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	product = models.ForeignKey( Product)
	productFeature = models.ForeignKey( Feature)


class PurchaseOrderItem( OrderItem):
	''' Purchase Order Item '''
	order = models.ForeignKey( PurchaseOrder )

class SalesOrderItem( OrderItem):
	''' Sales Order Item '''
	order = models.ForeignKey( SalesOrder )
