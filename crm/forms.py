from django import forms
from django.forms import ModelForm
from common.widgets import DatePickerWidget
from party.models import Party

customer_type_choices =(
	('Person','Person'),
	('Organization', 'Organization'),
)
class CustomerForm( ModelForm):
	first_name = forms.CharField()
	middle_name = forms.CharField()
	last_name = forms.CharField()
	name = forms.CharField()
	customer_type = forms.ChoiceField( choices=customer_type_choices, widget=forms.RadioSelect)
	class Meta:
		model=Party
		exclude=('classification', 'customer_type',)
