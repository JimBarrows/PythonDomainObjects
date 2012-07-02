from datetime import datetime

from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView

from products.forms import *
from products.models import *

CategoryClassificationFormSet = inlineformset_factory( Product, CategoryClassification, extra=1, form=CategoryClassificationForm)

class ProductsList( ListView):
	pass

def add_product_formsets_to_context( view, context):
	if view.request.POST:
		context['category_list'] = CategoryClassificationFormSet( view.request.POST, instance=view.object)
	else :
		context['category_list'] = CategoryClassificationFormSet( instance=view.object)
	return context

def save_product_formsets( context, instance):
	category_list = context['category_list']
	category_list.instance = instance
	category_list.save()

def product_formsets_are_valid( context):
	return context['category_list'].is_valid()

class ProductsCreate( CreateView):

	def get_context_data(self, **kwargs):
		context = super(ProductsCreate, self).get_context_data( **kwargs)
		context = add_product_formsets_to_context( self, context)
		return context

	def form_valid( self, form):
		context = self.get_context_data()
		self.object = form.save()
		save_product_formsets( context, self.object)
		return HttpResponseRedirect(self.get_success_url())

class ProductUpdate( UpdateView):

	def get_context_data(self, **kwargs):
		context = super(ProductUpdate, self).get_context_data( **kwargs)
		context = add_product_formsets_to_context( self, context)
		return context

	def form_valid( self, form):
		context = self.get_context_data()
		self.object = form.save()
		if product_formsets_are_valid(context) :
			save_product_formsets( context, self.object)
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data( form=form))

class ProductDelete( DeleteView):
	pass

class ProductsDetail( DetailView):
	pass

class CategoryList( ListView):
	model=CategoryClassification
	queryset=CategoryClassification.objects.all()

class CategoryCreate( CreateView):
	model=CategoryClassification
	form_class=CategoryClassificationForm
	success_url="/products/classifications"

class CategoryDetail( DetailView):
	model=CategoryClassification

class CategoryUpdate( UpdateView):
	model=CategoryClassification
	form_class=CategoryClassificationForm
	success_url='/products/classifications'

class CategoryDelete( DeleteView):
	model=CategoryClassification
	success_url='/products/classifications'

class PricingComponentList( ListView):
	model=PriceComponent
	queryset=PriceComponent.objects.all()

class PricingComponentCreate( CreateView):
	model=PriceComponent
	form_class=PriceComponentForm
	success_url="/products/pricing"

class PricingComponentDetail( DetailView):
	model=PriceComponent

class PricingComponentUpdate( UpdateView):
	model=PriceComponent
	form_class=PriceComponentForm
	success_url="/products/pricing"

class PricingComponentDelete( DeleteView):
	model=PriceComponent
	success_url="/products/pricing"

class EstimatedProductCostList( ListView):
	model=EstimatedProductCost
	queryset=EstimatedProductCost.objects.all()

class EstimatedProductCostCreate( CreateView):
	model=EstimatedProductCost
	form_class=EstimatedProductCostForm
	success_url="/products/costing"

class EstimatedProductCostDetail( DetailView):
	model=EstimatedProductCost

class EstimatedProductCostUpdate( UpdateView):
	model=EstimatedProductCost
	form_class=EstimatedProductCostForm
	success_url="/products/costing"

class EstimatedProductCostDelete( DeleteView):
	model=EstimatedProductCost
	success_url="/products/costing"
