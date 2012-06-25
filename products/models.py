from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from polymorphic import PolymorphicModel
from party.models import PartyType
from datetime import datetime
from party.models import Organization, Facility, PartyRole, GeographicBoundary

class Product(PolymorphicModel):
	name = models.CharField(max_length=250)
	introduction_date = models.DateField(blank=True, null=True)
	sales_discontinuation_date = models.DateField(blank=True, null=True)
	support_discontinuation_date = models.DateField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	categories = models.ManyToManyField( 'Category', through='CategoryClassification', blank=True, null=True)
	manufactured_by = models.ForeignKey(Organization, related_name='producerOf_set', blank=True, null=True)
	suppliers = models.ManyToManyField( Organization, through='SupplierProduct', blank=True, null=True)
	def __unicode__(self):
		return self.name
	class Meta:
		ordering=['name']
		

class Good(Product):
	identifiers = models.ManyToManyField( 'IdentificationType', through='Identification', blank=True, null=True)
	finished_good = models.ForeignKey('FinishedGood', blank=True, null=True)
	def __unicode__(self):
		return self.name

class Service(Product):
	def __unicode__(self):
		return self.name

class Part(PolymorphicModel):
	name = models.CharField(max_length=250)

class FinishedGood( Part) :
	''' A finished good ready for sale.'''

class SubAssembly( Part) :
	''' A sub assembly of a finished good.'''

class RawMaterial( Part) :
	''' A raw material.'''

class PartBom( models.Model):
	from_date = models.DateField()
	thru_date = models.DateField(blank=True, null=True)
	quantity_used = models.IntegerField()
	instruction = models.TextField()
	comment = models.TextField()
	

class ProductAssociation( models.Model):
	from_date = models.DateField()
	thru_date = models.DateField(blank=True, null=True)
	kind = models.ForeignKey('ProductAssociationType')
	from_product = models.ForeignKey(Product, related_name='fromAssociation_set')
	to_product = models.ForeignKey(Product, related_name='toAssociation_set')

class ProductAssociationType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class EstimatedProductCost( PolymorphicModel):
	from_date = models.DateField()
	thru_date = models.DateField(blank=True, null=True)
	cost = models.DecimalField( max_digits=8, decimal_places=2)
	feature = models.ForeignKey('Feature', blank=True, null=True)
	product = models.ForeignKey('Product', blank=True, null=True)
	kind = models.ForeignKey('CostComponentType')
	geographic_boundary = models.ForeignKey(GeographicBoundary, blank=True, null=True)
	organization = models.ForeignKey(Organization, related_name='estimatedProductCost_set')

class CostComponentType( models.Model):
	description = models.CharField(max_length=250)

class PriceComponent( PolymorphicModel):
	product = models.ForeignKey('Product', blank=True, null=True)
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank=True, null=True)
	comment = models.TextField(blank=True, null=True)
	geographic_boundary = models.ForeignKey(GeographicBoundary, blank=True, null=True)
	party_type = models.ForeignKey(PartyType, blank=True, null=True)
	product_category = models.ForeignKey('Category', blank=True, null=True) 
	quantity_break = models.ForeignKey('QuantityBreak', blank=True, null=True)
	order_value = models.ForeignKey('OrderValue', blank=True, null=True)
	sales_type = models.ForeignKey('SaleType', blank=True, null=True)
	specified_for = models.ForeignKey(Organization, blank=True, null=True)
	feature = models.ForeignKey('Feature', blank=True, null=True)
	currency = models.ForeignKey('CurrencyMeasure', blank=True, null=True)
	part = models.ForeignKey('Part', blank=True, null=True)
	def __unicode__(self):
		return self.comment
	class Meta:
		abstract = True

class BasePrice( PriceComponent):
	''' A starting point for figuring out the price. ''' 
	price = models.DecimalField( max_digits=8, decimal_places=2)

class DiscountComponent( PriceComponent):
	''' Discounts that can occur. '''
	percent = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])

class SurchargeComponent( PriceComponent):
	''' Discounts that can occur. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)
	percent = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])

class ManufacturerSuggestedPrice( PriceComponent):
	''' Not necessarily the price being charged. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)

class OneTimeCharge( PriceComponent):
	''' Not necessarily the price being charged. '''
	price = models.DecimalField( max_digits=8, decimal_places=2)
	percent = models.IntegerField( validators=[MaxValueValidator(100), MinValueValidator(0)])

class RecurringCharge( PriceComponent):
	per = models.ForeignKey('TimeFrequencyMeasure')
	price = models.DecimalField( max_digits=8, decimal_places=2)

class UtilizationCharge( PriceComponent):
	per = models.ForeignKey('UnitOfMeasure', related_name="per_set")
	quantity = models.IntegerField()
	price = models.DecimalField( max_digits=8, decimal_places=2)

class SaleType( models.Model):
	description = models.CharField(max_length=250)

class OrderValue( models.Model):
	from_value = models.DecimalField( max_digits=9, decimal_places=2)
	thru_value = models.DecimalField( max_digits=9, decimal_places=2)

class QuantityBreak( models.Model):
	from_quantity = models.IntegerField()
	thru_quantity = models.IntegerField()
	def __unicode__(self):
		return '{0} - {1}'.format( self.from_quantity, self.thru_quantity )
	class Meta:
		ordering = ['from_quantity', 'thru_quantity']

class InventoryItem( PolymorphicModel ):
	good = models.ForeignKey('Good') 
	status = models.ForeignKey('InventoryItemStatusType') 
	located_at = models.ForeignKey(Facility) 
	located_within = models.ForeignKey('Container') 
	part = models.ForeignKey('Part') 
	lot = models.ForeignKey('Lot') 
	quantity_on_hand = models.IntegerField()
	serial_number = models.CharField(max_length=250)
	def __unicode__(self):
		return quantity_on_hand if (quantity_on_hand == null) else serial_number

class InventoryItemVariance( models.Model):
	physical_inventory_date = models.DateField()
	quantity = models.IntegerField();
	comment = models.CharField(max_length=250)
	reason = models.ForeignKey('Reason') 
	adjustment_for = models.ForeignKey('InventoryItem') 
	def __unicode__(self):
		return self.comment

class Reason( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class Container( models.Model):
	description = models.CharField(max_length=250)
	located_at = models.ForeignKey(Facility) 
	kind = models.ForeignKey('ContainerType') 
	
class ContainerType( models.Model):
	description = models.CharField(max_length=250)

class Lot( models.Model):
	description = models.CharField(max_length=250)
	quantity = models.IntegerField()
	creation_date = models.DateField(default = datetime.today())
	expiration_date = models.DateField(blank=True, null=True)

class InventoryItemStatusType( models.Model):
	description = models.CharField(max_length=250)

#class ReorderGuideline( models.Model):
#	guidelineFor = models.ForeignKey('Good')
#	from_date = models.DateField(default = datetime.today())
#	thru_date = models.DateField(blank=True, null=True)
#	reorder_quantity = models.IntegerField()
#	reorder_level = models.IntegerField()
#	boundary = models.ForeignKey(GeographicBoundary, blank=True, null=True)
#	facility = models.ForeignKey(Facility, blank=True, null=True)
#	internal_organization = models.ForeignKey(PartyRole, blank=True, null=True, limit_choices_to={'party_role_type__description':'Internal Organization'})
#	part = models.ForeignKey('Part')
	
class SupplierProduct( models.Model):
	product = models.ForeignKey('Product')
	organization = models.ForeignKey(Organization)
	available_from = models.DateField(default = datetime.today())
	available_thru = models.DateField(blank=True, null=True)
	standard_lead_time_in_days = models.IntegerField(blank=True, null=True)
	preference = models.ForeignKey('PreferenceType', blank=True, null=True)
	rating = models.ForeignKey('RatingType', blank=True, null=True)
	part = models.ForeignKey('Part', blank=True, null=True)
	def __unicode__(self):
		return self.organization.name

class PreferenceType( models.Model):
	description = models.CharField(max_length=250)

class RatingType( models.Model):
	description = models.CharField(max_length=250)

class Identification( models.Model ):
	value = models.CharField(max_length=250)
	good = models.ForeignKey(Good)
	kind = models.ForeignKey('IdentificationType')
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.value

class CategoryClassification( models.Model ):
	product = models.ForeignKey(Product)
	category_type = models.ForeignKey('Category')
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	primary = models.BooleanField()
	comment = models.TextField( blank = True, null = True)
	def __unicode__(self):
		return self.category_type.description

class Feature( PolymorphicModel ):
	description = models.CharField(max_length=250)
	category = models.ForeignKey('FeatureCategory')
	product = models.ManyToManyField('Product', through='FeatureApplicability')
	def __unicode__(self):
		return self.description

class Dimension( Feature ) :
	number_specified =models.IntegerField()
	measured_using = models.ForeignKey('UnitOfMeasure')
	def __unicode__(self):
		return '{0} {1}'.format( self.number_specified, self.measured_using.abbreviation)

class UnitOfMeasure( PolymorphicModel):
	abbreviation = models.CharField(max_length=15)
	description = models.CharField(max_length=100)
	def __unicode__(self):
		return self.abbreviation 
	class Meta:
		ordering=['abbreviation', 'description']

class TimeFrequencyMeasure( UnitOfMeasure):
	def __unicode__(self):
		return self.abbreviation 

class CurrencyMeasure( UnitOfMeasure):
	def __unicode__(self):
		return self.abbreviation 

class UnitOfMeasureConversion( models.Model):
	convert_from = models.ForeignKey('UnitOfMeasure', related_name='convert_from_set')
	convert_to = models.ForeignKey('UnitOfMeasure', related_name='convertInto_set')
	conversion_factor = models.DecimalField( max_digits=5, decimal_places=3)
	def __unicode__(self):
		return '{0} * {1} = {2}'.format( self.convert_from.abbreviation, self.conversion_factor, self.convert_to.abbreviation)

class FeatureApplicability( models.Model) :
	ApplicabilityChoices = (
		('Required' , 'Required'),
		('Standard' , 'Standard'),
		('Optional' , 'Optional'),
		('Selectable' , 'Selectable')
		)
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	product = models.ForeignKey('Product')
	feature = models.ForeignKey('Feature' )
	kind = models.CharField(max_length=10, choices=ApplicabilityChoices)
	def __unicode__(self):
		return self.feature.description

class FeatureInteraction( models.Model ):
	incompatibility = models.BooleanField()
	interaction_dependancy = models.BooleanField()
	of = models.ForeignKey('Feature', related_name='of_set')
	factor_in = models.ForeignKey('Feature', related_name='factor_in_set')
	context_of = models.ForeignKey('Product')

class Category(models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	of_interest_to = models.ManyToManyField( PartyType, through='MarketInterest')
	def __unicode__(self):
		return self.description

class MarketInterest( models.Model ):
	party_type = models.ForeignKey(PartyType)
	category_type = models.ForeignKey(Category)
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.party_type.description

class IdentificationType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class FeatureCategory( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
