from django.forms import ModelForm
from common.forms import CommonModelForm,make_custom_field
from products.models import Good
from products.models import Service

class GoodForm( CommonModelForm ):
	formfield_callback = make_custom_field 
	class Meta:
		model=Good

class ServiceForm( CommonModelForm ):
	formfield_callback = make_custom_field 
	class Meta:
		model=Service

