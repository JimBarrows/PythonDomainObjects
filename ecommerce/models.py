from django.db import models
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.core.validators import MaxValueValidator, MinValueValidator
from party.models import Party, WebAddress
from products.models import Feature, Product

class UserProfile( models.Model ):
	user = models.OneToOneField( User )
	preferences = models.ManyToManyField( 'PreferenceType', through='UserPreference')
	party = models.ForeignKey( Party )
	webAddress = models.ForeignKey( WebAddress )
	def __unicode__(self):
		return self.user.username

class LoginAccountHistory( models.Model ):
	username = models.CharField(max_length=30)
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	userProfile = models.ForeignKey( 'UserProfile' )


class PreferenceType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class UserPreference( models.Model ):
	value = models.CharField(max_length=250)
	userProfile = models.ForeignKey( 'UserProfile' )
	preferenceType = models.ForeignKey( 'preferenceType' )

class WebContent( models.Model ):
	description = models.TextField()
	content = models.TextField( blank=True, null = True)
	associated = models.ManyToManyField( 'WebContent', through='WebContentAssociation', blank=True, null = True)
	file = models.FileField(upload_to='content', blank=True, null = True)
	roles = models.ManyToManyField( 'WebContentRoleType', through='WebContentRole', blank=True, null = True)
	kind = models.ForeignKey( 'WebContentType')
	status = models.ForeignKey( 'WebContentStatusType')
	webAddress = models.ForeignKey( WebAddress )
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
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)


class WebContentAssociation( models.Model ):
	''' 0,0 is upper left '''
	x = models.IntegerField( validators=[MinValueValidator(0)])
	y = models.IntegerField( validators=[MinValueValidator(0)])
	fromContent = models.ForeignKey( 'WebContent', related_name = 'fromContent_set' )
	toContent = models.ForeignKey( 'WebContent', related_name = 'toContent_set' )
	function = models.ForeignKey( 'FunctionType' )

class FunctionType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

class WebObject( models.Model ):
	name = models.CharField(max_length=250)
	description = models.TextField( blank=True, null = True)
	file = models.FileField(upload_to='webObjects', blank=True, null = True)
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
	fromDate = models.DateField()
	thruDate = models.DateField(blank = True, null = True)
	webObject = models.ForeignKey( 'WebObject' )
	webContent = models.ForeignKey( 'WebContent' )

class PurposeType( models.Model ):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description

