from django.db import models
from party import *

class GeographicBoundaryType(models.Model):
	description = models.CharField(max_length=250, blank = True, null = True)
	def __unicode__(self):
		return self.description
	class Meta:
		app_label = 'party'

class GeographicBoundary(models.Model):
	name = models.CharField(max_length=250, blank = True, null = True)
	abbrev = models.CharField(max_length=10, blank = True, null = True)
	geocode = models.CharField(max_length=250, blank = True, null = True)
	geographic_boundary_type = models.ForeignKey(GeographicBoundaryType)
	def __unicode__(self):
		return self.name
	class Meta:
		app_label = 'party'

class GeographicBoundaryAssociation(models.Model):
	contains = models.ForeignKey(GeographicBoundary, related_name='contains_set')
	contained_by = models.ForeignKey(GeographicBoundary, related_name='contained_by_set')
	def __unicode__(self):
		return self.contained_by.name + " - " + self.contains.name 
	class Meta:
		app_label = 'party'

