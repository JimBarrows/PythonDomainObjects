from django.forms import ModelForm
from django.shortcuts import render_to_response
from django.core.context_processors import csrf

class CommonModelForm( ModelForm):
		error_css_class = 'error'


def render_form_to_response(  request, path, context ):
	context.update(csrf(request))
	return render_to_response( path, context)
