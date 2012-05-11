from django.db import models
from datetime import datetime

class GeneralLedgerAccount(models.Model):
	name = models.CharField(max_length=120)
	description = models.CharField(max_length=250)
	defined_by = models.ForeignKey( 'GeneralLedgerAccountType')
	associated_with = models.ManyToManyField( 'party.PartyRole', through='OrganizationGLAccount')
	def __unicode__(self):
		return 'General Ledger Account'
	class Meta:
		app_label="accounting"

class GeneralLedgerAccountType(models.Model):
	description = models.CharField(max_length=250)
	def __unicode__(self):
		return 'General Ledger Account Type'
	class Meta:
		app_label="accounting"

class OrganizationGLAccount(models.Model):
	from_date = models.DateField(default=datetime.today())
	thru_date = models.DateField(blank=True, null=True)
	for_gl = models.ForeignKey( 'GeneralLedgerAccount')
	for_internal_organization = models.ForeignKey( 'party.PartyRole')
	def __unicode__(self):
		return 'Organziation GL Account'
	class Meta:
		app_label="accounting"
