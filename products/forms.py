from django import forms
from django.forms import ModelForm
from products.models import Good, Service, CategoryClassification, PriceComponent
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
