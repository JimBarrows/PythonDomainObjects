from django import forms
from django.forms import ModelForm
from common.widgets import DatePickerWidget
from party.models import Party, OrganizationType

customer_type_choices =(
	('Person','Person'),
	('Organization', 'Organization'),
)

class CustomerForm( ModelForm):
	first_name = forms.CharField(required=False)
	middle_name = forms.CharField(required=False)
	last_name = forms.CharField(required=False)
	name = forms.CharField(required=False)
	customer_type = forms.ChoiceField( choices=customer_type_choices, widget=forms.RadioSelect, required=False)
	organization_type = forms.ModelChoiceField( queryset=OrganizationType.objects.all(), required=False)
	class Meta:
		model=Party
		exclude=('classification', 'customer_type',)
