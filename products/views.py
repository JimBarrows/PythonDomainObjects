from datetime import datetime

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from products.forms import *
from products.models import *

CategoryClassificationFormSet = inlineformset_factory( Good, CategoryClassification, extra=1)
SupplierFormSet = inlineformset_factory( Good, SupplierProduct, extra=1)

class ServicesList( ListView):
	model = Service
	queryset=  Service.objects.filter( 
		(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
		(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
		)

class ServicesCreate( CreateView):
	model=Service
	form_class=ServiceForm
	success_url='/products/services'

class ServicesUpdate( UpdateView):
	model=Service
	form_class=ServiceForm
	success_url='/products/services'

class ServicesDelete( DeleteView):
	model=Service
	success_url='/products/services'

