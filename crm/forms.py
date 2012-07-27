from django import forms
from django.forms import ModelForm
from common.widgets import DatePickerWidget
from party.models import Person

class PersonForm( ModelForm):
	class Meta:
		model=Person
		exclude=('classification',)
