from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from party.models import Party, PartyRole, PartyRoleType, ContactMechanism, GeographicBoundary
from products.models import Product, Feature, Category

class Order( PolymorphicModel ):
	orderDate = models.DateField()
	entryDate = models.DateField()

class PurchaseOrder( Order):
	''' Purchase Order '''
	placedBy = models.ForeignKey( PartyRole, related_name='placingCustomerPo_set' )
	takenBy = models.ForeignKey( PartyRole, related_name='internalOrganizationPo_set' )
	requestedBillTo = models.ForeignKey( PartyRole, related_name='billToCustomerPo_set' )
	placingLocation = models.ForeignKey( ContactMechanism, related_name='placingLocationPo_set' )
	locationForTaking = models.ForeignKey( ContactMechanism, related_name='locationForTakingPo_set' )
	billedTo = models.ForeignKey( ContactMechanism, related_name='billedTo_set' )

class SalesOrder( Order):
	''' Sales Order '''
	placedBy = models.ForeignKey( PartyRole, related_name='placingCustomerSo_set' )
	takenBy = models.ForeignKey( PartyRole, related_name='internalOrganizationSo_set' )
	requestedBillTo = models.ForeignKey( PartyRole, related_name='billToCustomerSo_set' )
	placingLocation = models.ForeignKey( ContactMechanism, related_name='placingLocationSo_set' )
	locationForTaking = models.ForeignKey( ContactMechanism, related_name='locationForTakingSo_set' )
	billedTo = models.ForeignKey( ContactMechanism, related_name='billedToSo_set' )

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
	shipTo = models.ForeignKey( ContactMechanism )
	shipToCustomer = models.ForeignKey( PartyRole )
	purchasedBy = models.ManyToManyField( 'PurchaseOrderItem')

class OrderRole( models.Model ):
	percentContribution = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])
	of = models.ForeignKey( Order )
	involving = models.ForeignKey( Party )
	describedBy = models.ForeignKey( 'OrderRoleType' )

class OrderRoleType( models.Model ):
	description = models.CharField(max_length=250)

class OrderAdjustment( models.Model):
	amount = models.DecimalField( max_digits=8, decimal_places=2 )
	percentage = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])
	kind = models.ForeignKey( 'OrderRoleType' )
	affectingItem = models.ForeignKey( 'OrderItem' )
	affectingOrder = models.ForeignKey( 'Order' )

class SalesTaxLookup( models.Model ):
	geographicBoundary = models.ForeignKey( GeographicBoundary )
	productCategory = models.ForeignKey( Category )
	percentage = models.DecimalField( max_digits=5, 
		decimal_places=2, 
		validators=[MaxValueValidator(100.00), MinValueValidator(0.00)]) 
	

class OrderAdjustmentType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class OrderTerm( models.Model ):
	value = models.DecimalField( max_digits=12, decimal_places=2) 
	conditionForItem = models.ForeignKey( OrderItem )
	conditionForOrder = models.ForeignKey( Order )
	describedBy = models.ForeignKey( 'OrderTermType' )
	

class OrderTermType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class OrderStatus( models.Model ):
	value = models.DecimalField( max_digits=12, decimal_places=2) 
	conditionForItem = models.ForeignKey( OrderItem )
	conditionForOrder = models.ForeignKey( Order )
	describedBy = models.ForeignKey( 'OrderStatusType' )
	

class OrderStatusType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

