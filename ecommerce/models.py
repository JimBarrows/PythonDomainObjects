from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.validators import MaxValueValidator, MinValueValidator
from party.models import Party, WebAddress, ContactMechanism, PartyRole, CommunicationEvent
from products.models import Feature, Product, Category
from orders.models import OrderItem

class UserProfile( models.Model ):
	user = models.OneToOneField( User )
	preferences = models.ManyToManyField( 'PreferenceType', through='UserPreference')
	party = models.ForeignKey( Party )
	web_address = models.ForeignKey( WebAddress )
	def __unicode__(self):
		return self.user.username

class LoginAccountHistory( models.Model ):
	username = models.CharField(max_length=30)
	from_date = models.DateField()
	thru_date = models.DateField(blank = True, null = True)
	user_profile = models.ForeignKey( 'UserProfile' )


class PreferenceType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class UserPreference( models.Model ):
	value = models.CharField(max_length=250)
	user_profile = models.ForeignKey( 'UserProfile' )
	preference_type = models.ForeignKey( 'PreferenceType' )

class WebContent( models.Model ):
	description = models.TextField()
	content = models.TextField( blank=True, null = True)
	associated = models.ManyToManyField( 'WebContent', through='WebContentAssociation', blank=True, null = True)
	file = models.FileField(upload_to='content', blank=True, null = True)
	roles = models.ManyToManyField( 'WebContentRoleType', through='WebContentRole', blank=True, null = True)
	kind = models.ForeignKey( 'WebContentType')
	status = models.ForeignKey( 'WebContentStatusType')
	web_address = models.ForeignKey( WebAddress )
	def __unicode__(self):
		return self.description

class WebContentRoleType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class WebContentStatusType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class WebContentType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class WebContentRole( models.Model ):
	content = models.ForeignKey( 'WebContent')
	role = models.ForeignKey( 'WebContentRoleType')
	party = models.ForeignKey( Party )
	from_date = models.DateField()
	thru_date = models.DateField(blank = True, null = True)


class WebContentAssociation( models.Model ):
	''' 0,0 is upper left '''
	x = models.IntegerField( validators=[MinValueValidator(0)])
	y = models.IntegerField( validators=[MinValueValidator(0)])
	from_content = models.ForeignKey( 'WebContent', related_name = 'from_content_set' )
	to_content = models.ForeignKey( 'WebContent', related_name = 'to_content_set' )
	function = models.ForeignKey( 'FunctionType' )

class FunctionType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class WebObject( models.Model ):
	name = models.CharField(max_length=250)
	description = models.TextField( blank=True, null = True)
	file = models.FileField(upload_to='web_objects', blank=True, null = True)
	features = models.ManyToManyField( Feature)
	usage = models.ManyToManyField( 'WebContent', through='ObjectUsage')
	purposes = models.ManyToManyField( 'PurposeType', blank=True, null = True)
	products = models.ManyToManyField( Product, blank=True, null = True)
	kind = models.ForeignKey( 'WebObjectType' )

class WebObjectType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class ObjectUsage( models.Model ):
	from_date = models.DateField()
	thru_date = models.DateField(blank = True, null = True)
	web_object = models.ForeignKey( 'WebObject' )
	web_content = models.ForeignKey( 'WebContent' )

class PurposeType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class Subscription( models.Model ):
	start = models.DateField()
	end = models.DateField()
	fullfilled_via = models.ManyToManyField( 'SubscriptionActivity' )
	orderItem = models.ForeignKey( OrderItem )
	kind = models.ForeignKey( 'SubscriptionType' )
	product = models.ForeignKey( Product )
	category = models.ForeignKey( Category )
	subscriber = models.ForeignKey( PartyRole )
	sent_to = models.ForeignKey( ContactMechanism )
	originating_from = models.ForeignKey( CommunicationEvent )

class SubscriptionActivity( models.Model ):
	date_sent = models.DateField()
	comment = models.TextField()
	
class SubscriptionType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

