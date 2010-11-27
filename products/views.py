from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from common.forms import CommonModelForm
from django.forms import DateField
from common.widgets import DatePickerWidget

def index( request):
	c = {}
	return render_to_response('products/index.html', c)

