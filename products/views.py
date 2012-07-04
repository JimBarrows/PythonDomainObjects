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
IdentificationFormSet = inlineformset_factory( Good, Identification, extra=1, form=IdentificationForm)

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

def add_good_formsets_to_context( view, context):
	if view.request.POST:
		context['identification_list'] = IdentificationFormSet( view.request.POST, instance=view.object)
	else :
		context['identification_list'] = IdentificationFormSet( instance=view.object)
	return context

def save_good_formsets( context, instance):
		context['identification_list'].instance=instance
		context['identification_list'].save()
		save_product_formsets( context, instance)

class ProductCreate( CreateView):

	def get_context_data(self, **kwargs):
		context = super(ProductCreate, self).get_context_data( **kwargs)
		return add_product_formsets_to_context( self, context)

	def form_valid( self, form):
		context = self.get_context_data()
		if product_formsets_are_valid( context):
			self.object = form.save()
			save_product_formsets( context, self.object)
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

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

class ProductDetail( DetailView):
	def get_context_data(self, **kwargs):
		context = super(ProductDetail,self).get_context_data(**kwargs)
		context['category_list']=CategoryClassification.objects.filter(product=self.object)
		return context

class GoodCreate( ProductCreate):

	def get_context_data(self, **kwargs):
		context = super(GoodCreate, self).get_context_data( **kwargs)
		return add_good_formsets_to_context( self, context)

	def form_valid( self, form):
		context = self.get_context_data()
		if product_formsets_are_valid( context) and context['identification_list'].is_valid() :
			self.object = form.save()
			save_product_formsets( context, self.object)
			save_good_formsets( context, self.object)
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class GoodUpdate( ProductUpdate):

	def get_context_data(self, **kwargs):
		context = super(GoodUpdate, self).get_context_data( **kwargs)
		return add_good_formsets_to_context( self, context)

	def form_valid( self, form):
		context = self.get_context_data()
		if product_formsets_are_valid( context) and context['identification_list'].is_valid() :
			self.object = form.save()
			save_product_formsets( context, self.object)
			save_good_formsets( context, self.object)
			return HttpResponseRedirect(self.get_success_url())
		else:
			return self.render_to_response(self.get_context_data(form=form))

class GoodDetail( ProductDetail):
	def get_context_data(self, **kwargs):
		context = super(ProductDetail,self).get_context_data(**kwargs)
		context['identification_list']=Identification.objects.filter(good=self.object)
		return context

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
