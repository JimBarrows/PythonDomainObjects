from django.db import models
from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

def make_custom_field(f):
	formfield = f.formfield()
	if isinstance(f, models.DateField):
		formfield.widget.format = '%m/%d/%Y'
		formfield.widget.attrs.update({'class':'dateFieldPicker', 'readonly':'true'})
	return formfield

class CommonModelForm( ModelForm):
	error_css_class = 'error'
#Note: because of https://code.djangoproject.com/ticket/12915 you have to copy the following  line to every implementing class :(
#	formfield_callback = make_custom_field

def render_form_to_response(  request, path, context ):
	context.update(csrf(request))
	return render_to_response( path, context)
