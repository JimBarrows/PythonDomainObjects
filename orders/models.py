from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from party.models import Party, PartyRole, PartyRoleType, ContactMechanism, GeographicBoundary
from products.models import Product, Feature, Category

class Order( PolymorphicModel ):
	order_date = models.DateField()
	entry_date = models.DateField()

class PurchaseOrder( Order):
	placed_by = models.ForeignKey( PartyRole, related_name='placingCustomerPo_set' )
	taken_by = models.ForeignKey( PartyRole, related_name='internalOrganizationPo_set' )
	requested_bill_to = models.ForeignKey( PartyRole, related_name='billToCustomerPo_set' )
	placing_location = models.ForeignKey( ContactMechanism, related_name='placing_locationPo_set' )
	location_for_taking = models.ForeignKey( ContactMechanism, related_name='location_for_takingPo_set' )
	billed_to = models.ForeignKey( ContactMechanism, related_name='billed_to_set' )

class SalesOrder( Order):
	placed_by = models.ForeignKey( PartyRole, related_name='placingCustomerSo_set' )
	taken_by = models.ForeignKey( PartyRole, related_name='internalOrganizationSo_set' )
	requested_bill_to = models.ForeignKey( PartyRole, related_name='billToCustomerSo_set' )
	placing_location = models.ForeignKey( ContactMechanism, related_name='placing_locationSo_set' )
	location_for_taking = models.ForeignKey( ContactMechanism, related_name='location_for_takingSo_set' )
	billed_to = models.ForeignKey( ContactMechanism, related_name='billed_toSo_set' )

class OrderItem( models.Model ):
	quantity = models.IntegerField(),
	unit_price = models.DecimalField( max_digits=8, decimal_places=2 )
	estimated_delivery_date = models.DateField()
	shipping_instructions = models.TextField()
	item_description = models.TextField()
	comment = models.TextField()
	ordered_with = models.ForeignKey('self', blank = True, null = True, related_name='child_set' )
	product = models.ForeignKey( Product )
	product_feature = models.ForeignKey( Feature )


class PurchaseOrderItem( OrderItem):
	''' Purchase Order Item '''
	order = models.ForeignKey( PurchaseOrder )
	ship_to = models.ForeignKey( ContactMechanism )
	ship_to_customer = models.ForeignKey( PartyRole )

class SalesOrderItem( OrderItem):
	''' Sales Order Item '''
	order = models.ForeignKey( SalesOrder )
	ship_to = models.ForeignKey( ContactMechanism )
	ship_to_customer = models.ForeignKey( PartyRole )
	purchased_by = models.ManyToManyField( 'PurchaseOrderItem')

class OrderRole( models.Model ):
	percent_contribution = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])
	of = models.ForeignKey( Order )
	involving = models.ForeignKey( Party )
	described_by = models.ForeignKey( 'OrderRoleType' )

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
	described_by = models.ForeignKey( 'OrderTermType' )
	

class OrderTermType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class OrderStatus( models.Model ):
	value = models.DecimalField( max_digits=12, decimal_places=2) 
	conditionForItem = models.ForeignKey( OrderItem )
	conditionForOrder = models.ForeignKey( Order )
	described_by = models.ForeignKey( 'OrderStatusType' )
	

class OrderStatusType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

