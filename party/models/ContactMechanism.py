from django.db import models
from Party import Party, PartyRoleType
from GeographicBoundary import GeographicBoundary

class ContactMechanismPurposeType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class ContactMechanism(models.Model):
	comment = models.TextField( blank = True, null = True)
	def __unicode__(self):
		return 'Contact Mechanism'
	class Meta:
		app_label = 'party'

class PartyContactMechanism(models.Model):
	party = models.ForeignKey(Party)
	contact_mechanism = models.ForeignKey(ContactMechanism)
	party_role_type = models.ForeignKey(PartyRoleType, blank=True, null=True)
	purpose = models.ManyToManyField( ContactMechanismPurposeType, through='PartyContactMechanismPurpose')
	comment = models.TextField(blank=True, null=True)
	from_date = models.DateField()
	thru_date = models.DateField(blank = True, null = True)
	accepts_solicitations = models.BooleanField()
	class Meta:
		app_label = 'party'

class PartyContactMechanismPurpose(models.Model):
	contact_mechanism = models.ForeignKey(PartyContactMechanism)
	contact_mechanismType = models.ForeignKey(ContactMechanismPurposeType)
	from_date = models.DateField()
	thru_date = models.DateField(blank = True, null = True)
	def __unicode__(self):
		return self.contact_mechanismType.description
	class Meta:
		app_label = 'party'

class PostalAddress(ContactMechanism):
	street1 = models.CharField(max_length=250, )
	street2 = models.CharField(max_length=250, blank = True, null = True)
	directions = models.TextField( blank = True, null = True)
	def __unicode__(self):
		return self.street1
	class Meta:
		app_label = 'party'

class PostalAddressBoundary(models.Model):
	specified_for = models.ForeignKey(PostalAddress, related_name='specified_for')
	in_boundary = models.ForeignKey(GeographicBoundary, related_name='in_boundary')
	def __unicode__(self):
		return self.specified_for.street1 + " - " + self.in_boundary.name
	class Meta:
		app_label = 'party'
	

class EmailAddress( ContactMechanism):
	email = models.EmailField()
	def __unicode__(self):
		return self.email
	class Meta:
		app_label = 'party'

class IpAddress( ContactMechanism):
	ip_address = models.IPAddressField()
	def __unicode__(self):
		return self.ip_address
	class Meta:
		app_label = 'party'

class WebAddress( ContactMechanism):
	url = models.URLField()
	def __unicode__(self):
		return self.url
	class Meta:
		app_label = 'party'

class PhoneNumber( ContactMechanism):
	country_code = models.CharField(max_length=7)
	area_code = models.CharField(max_length=7)
	number = models.CharField(max_length=15)
	extension = models.CharField(max_length=15)
	def __unicode__(self):
		return '+{} ({}) {} {}'.format(country_code, area_code, number, extendsion)
	class Meta:
		app_label = 'party'
