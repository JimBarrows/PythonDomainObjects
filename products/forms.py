from django import forms
from django.forms import ModelForm
from products.models import *
from common.widgets import DatePickerWidget

class GoodForm( ModelForm ):
	introduction_date = forms.DateField(widget=DatePickerWidget, required=False)
	sales_discontinuation_date = forms.DateField(widget=DatePickerWidget, required=False)
	support_discontinuation_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=Good
		exclude=('categories', 'suppliers', 'identifiers')

class ServiceForm( ModelForm ):
	introduction_date = forms.DateField(widget=DatePickerWidget, required=False)
	sales_discontinuation_date = forms.DateField(widget=DatePickerWidget, required=False)
	support_discontinuation_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=Service
		exclude=('categories', 'suppliers',)

class CategoryClassificationForm( ModelForm):
	from_date = forms.DateField(widget=DatePickerWidget, required=True)
	thru_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=CategoryClassification

class PriceComponentForm( ModelForm):
	from_date = forms.DateField(widget=DatePickerWidget, required=True)
	thru_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=PriceComponent

class BasePriceForm( PriceComponentForm):
	class Meta:
		model=BasePrice

class DiscountComponentForm( PriceComponentForm):
	class Meta:
		model=DiscountComponent

class SurchargeComponentForm( PriceComponentForm):
	class Meta:
		model=SurchargeComponent

class ManufacturersSuggestedRetailPriceForm( PriceComponentForm):
	class Meta:
		model=ManufacturersSuggestedRetailPrice

class OneTimeChargeForm( PriceComponentForm):
	class Meta:
		model=OneTimeCharge

class RecurringChargeForm( PriceComponentForm):
	class Meta:
		model=RecurringCharge

class UtilizationChargeForm( PriceComponentForm):
	class Meta:
		model=UtilizationCharge

class EstimatedProductCostForm( ModelForm):
	from_date = forms.DateField(widget=DatePickerWidget, required=True)
	thru_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=EstimatedProductCost

class IdentificationForm( ModelForm):
	from_date = forms.DateField(widget=DatePickerWidget, required=True)
	thru_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=Identification

class FeatureForm( ModelForm):
	class Meta:
		model=Feature
		exclude=( 'product',)

class FeatureApplicabilityForm( ModelForm):
	from_date = forms.DateField(widget=DatePickerWidget, required=True)
	thru_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=FeatureApplicability

class ProductQualityForm( ModelForm):
	class Meta:
		model=ProductQuality
		exclude=( 'product',)
