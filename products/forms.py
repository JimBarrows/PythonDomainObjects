from django import forms
from django.forms import ModelForm
from products.models import Good
from products.models import Service
from common.widgets import DatePickerWidget

class GoodForm( ModelForm ):
	class Meta:
		model=Good

class ServiceForm( ModelForm ):
	introduction_date = forms.DateField(widget=DatePickerWidget, required=False)
	sales_discontinuation_date = forms.DateField(widget=DatePickerWidget, required=False)
	support_discontinuation_date = forms.DateField(widget=DatePickerWidget, required=False)
	class Meta:
		model=Service
		exclude=('categories', 'suppliers',)

