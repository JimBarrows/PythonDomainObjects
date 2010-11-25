from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from party.models import Party, PartyRole, PartyRoleType, ContactMechanism
from products.models import Product, Feature

class Order( PolymorphicModel ):
	orderDate = models.DateField()
	entryDate = models.DateField()

class PurchaseOrder( Order):
	''' Purchase Order '''

class SalesOrder( Order):
	''' Sales Order '''
	placedBy = models.ForeignKey( PartyRole, related_name='placingCustomer_set' )
	takenBy = models.ForeignKey( PartyRole, related_name='internalOrganization_set' )
	requestedBillTo = models.ForeignKey( PartyRole, related_name='billToCustomer_set' )
	placingLocation = models.ForeignKey( ContactMechanism, related_name='placingLocation_set' )
	locationForTaking = models.ForeignKey( ContactMechanism, related_name='locationForTaking_set' )
	billedTo = models.ForeignKey( ContactMechanism, related_name='billedTo_set' )

class OrderItem( models.Model ):
	quantity = models.IntegerField(),
	unitPrice = models.DecimalField( max_digits=8, decimal_places=2 )
	estimatedDeliveryDate = models.DateField()
	shippingInstructions = models.TextField()
	itemDescription = models.TextField()
	comment = models.TextField()
	orderedWith = models.ForeignKey('self', blank = True, null = True, related_name='child_set' )
	product = models.ForeignKey( Product )
	productFeature = models.ForeignKey( Feature )


class PurchaseOrderItem( OrderItem):
	''' Purchase Order Item '''
	order = models.ForeignKey( PurchaseOrder )
	shipTo = models.ForeignKey( ContactMechanism )
	shipToCustomer = models.ForeignKey( PartyRole )

class SalesOrderItem( OrderItem):
	''' Sales Order Item '''
	order = models.ForeignKey( SalesOrder )

class OrderRole( models.Model ):
	percentContribution = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])
	of = models.ForeignKey( Order )
	involving = models.ForeignKey( Party )
	describedBy = models.ForeignKey( 'OrderRoleType' )

class OrderRoleType( models.Model ):
	description = models.CharField(max_length=250)

