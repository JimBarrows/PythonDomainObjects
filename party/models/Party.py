from django.db import models
from polymodels.models import PolymorphicModel
from datetime import datetime

class Party(PolymorphicModel):
	classification = models.ManyToManyField( 'PartyType', through='PartyClassification')

	def findRoleByName(self, name):
		return self.partyrole_set.filter( party_role_type__description__exact=name).get()

	def __unicode__(self):
		return 'Party'

	class Meta:
		app_label = 'party'

class Person( Party):
	first_name=models.CharField(max_length=128)
	middle_name = models.CharField(max_length=128, blank=True, null = True)
	last_name = models.CharField(max_length=128)

	def __unicode__(self):
		return '{0}, {1} {2}'.format( self.last_name, self.first_name, self.middle_name)

	class Meta:
		app_label = 'party'
		verbose_name_plural = 'People'

class Organization( Party):
	name=models.CharField(max_length=128)

	def __unicode__(self):
		return self.name

	class Meta:
		app_label = 'party'
		verbose_name_plural = 'Organizations'

class PartyType(PolymorphicModel):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')

	def __unicode__(self):
		return self.description

	class Meta:
		app_label = 'party'
		verbose_name_plural = 'Party Types'

class OrganizationType(PartyType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class MinorityClassificationType(OrganizationType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class IndustryClassificationType(OrganizationType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class SizeClassificationType(OrganizationType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class PersonType(PartyType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class EeocClassificationType(PersonType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class IncomeClassificationType(PersonType):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class PartyClassification(PolymorphicModel):
	party = models.ForeignKey(Party)
	party_type = models.ForeignKey(PartyType)
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.party_type.description
	class Meta:
		app_label = 'party'
		verbose_name_plural = 'Party Classifications'
		verbose_name = 'Party Classification'

class OrganizationClassification(PartyClassification):
	'''Base Classification for organizations'''
	class Meta:
		app_label = 'party'

class MinorityClassification(OrganizationClassification):
	'''Base Classification for Minorities'''
	class Meta:
		app_label = 'party'

class IndustryClassification(OrganizationClassification):
	'''Base Classification for Industries'''
	class Meta:
		app_label = 'party'

class SizeClassification(OrganizationClassification):
	'''Base Classification for Sizing an organization'''
	class Meta:
		app_label = 'party'

class PersonClassification(PartyClassification):
	'''Base Classification for people'''
	class Meta:
		app_label = 'party'

class EeocClassification(PersonClassification):
	'''Base Classification for people'''
	class Meta:
		app_label = 'party'

class IncomeClassification(PersonClassification):
	'''Base Classification for people'''
	class Meta:
		app_label = 'party'

class PartyRoleType( models.Model):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	parties = models.ManyToManyField( 'Party', through='PartyRole')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'
		verbose_name = 'Party Role Type'
		verbose_name_plural = 'Party Role Types'
		ordering = ['description']

class PartyRole(models.Model):
	party = models.ForeignKey(Party)
	party_role_type = models.ForeignKey(PartyRoleType)
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return u'%s - %s' % (unicode( self.party), self.party_role_type.description)
	class Meta:
		app_label = 'party'
		verbose_name = 'Party Role'
		verbose_name_plural = 'Party Roles'

class PartyRelationshipType(models.Model):
	name = models.CharField(max_length=250)
	description = models.TextField(max_length=250, blank = True, null = True)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')
	from_role_type = models.ForeignKey(PartyRoleType, related_name='from_role_type_set')
	to_role_type = models.ForeignKey(PartyRoleType, related_name='to_role_type_set')
	def __unicode__(self):
		return self.name
	class Meta:
		app_label = 'party'
		verbose_name = 'Party Relationship Type'
		verbose_name_plural = 'Party Relationship Types'

class PartyRelationship(models.Model):
	comment = models.TextField()
	relationship_type = models.ForeignKey(PartyRelationshipType)
	from_date = models.DateField( default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	from_role = models.ForeignKey(PartyRole, related_name='from_role_set')
	to_role = models.ForeignKey(PartyRole, related_name='to_role_set')
	priority = models.ForeignKey('PriorityType', blank=True, null = True)
	status = models.ForeignKey('StatusType', blank=True, null = True)
	def __unicode__(self):
		return self.comment
	class Meta:
		app_label = 'party'
		verbose_name = 'Party Relationship'
		verbose_name_plural = 'Party Relationships'

class PartyPostalAddress(models.Model):
	party = models.ForeignKey(Party)
	comment = models.TextField()
	from_date = models.DateField( default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	location = models.ForeignKey('PostalAddress')
	def __unicode__(self):
		return self.location.street1
	class Meta:
		app_label = 'party'
		verbose_name = 'Party Postal Address'
		verbose_name_plural = 'Party Postal Addresss'

class PriorityType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'
		verbose_name = 'Priority Type '
		verbose_name_plural = 'Priority Types'

class StatusType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'
		verbose_name = 'Status Type '
		verbose_name_plural = 'Status Types'

class IdentificationType(PolymorphicModel):
	description = models.CharField(max_length=250)
	parent = models.ForeignKey('self', blank = True, null = True, related_name='child_set')

	def __unicode__(self):
		return self.description

	class Meta:
		app_label = 'party'

class Identifier(models.Model):
	party = models.ForeignKey(Party)
	identification_type = models.ForeignKey(IdentificationType)
	value = models.CharField(max_length=250)
	from_date = models.DateField(default = datetime.today())
	thru_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return u'%s - %s -%s' % (unicode( self.party), self.value, self.identification_type.description)
	class Meta:
		app_label = 'party'

