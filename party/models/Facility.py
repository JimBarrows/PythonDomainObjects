from django.db import models
from Party import Party
from ContactMechanism import ContactMechanism

class FacilityType( models.Model):
	description = models.CharField(max_length=250)
	kind_of = models.ForeignKey('self', blank = True, null = True, related_name='subType')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class FacilityRoleType( models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class Facility( models.Model):
	description = models.CharField(max_length=250)
	square_footage = models.IntegerField( blank=True, null = True)
	facility_type = models.ForeignKey(FacilityType)
	part_of = models.ForeignKey('self', blank = True, null = True, related_name='madeUpOf')
	roles = models.ManyToManyField( FacilityRoleType, through='FacilityRole')
	contact_mechanisms = models.ManyToManyField( ContactMechanism, through='FacilityContactMechanism')
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class FacilityContactMechanism(models.Model):
	facility = models.ForeignKey(Facility)
	contact_mechanism = models.ForeignKey(ContactMechanism)
	comment = models.TextField(blank=True, null=True)
	from_date = models.DateField()
	thru_date = models.DateField(blank = True, null = True)
	accepts_solicitations = models.BooleanField()
	class Meta:
		app_label = 'party'


class FacilityRole( models.Model):
	party = models.ForeignKey(Party, blank=True, null=True)
	facility = models.ForeignKey(Facility)
	role_type = models.ForeignKey(FacilityRoleType)
	from_date = models.DateField()
	thru_date = models.DateField( blank=True, null=True)
	class Meta:
		app_label = 'party'

