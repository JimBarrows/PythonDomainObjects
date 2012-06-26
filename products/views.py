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

#@login_required
#def good_index( request ) :
#	current_goods = Good.objects.filter( 
#			(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
#			(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
#		)
#	future_goods = Good.objects.filter( 
#			Q(introduction_date__gte = datetime.now()) 
#		)
#	past_goods = Good.objects.filter( 
#			Q(sales_discontinuation_date__lte=datetime.now()) 
#		)
#	return render_to_response('products/goods/index.html', {
#			'current_goods':current_goods, 
#			'future_goods':future_goods,
#			'past_goods':past_goods
#		})

#@login_required
#def service_index( request ) :
#	current_services = Service.objects.filter( 
#		(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
#		(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
#		)
#	future_services = Service.objects.filter( 
#		Q(introduction_date__gte = datetime.now()) 
#		)
#	past_services = Service.objects.filter( 
#		Q(sales_discontinuation_date__lte=datetime.now()) 
#		)
#	return render_to_response('products/services/index.html', {
#			'current_services':current_services, 
#			'future_services':future_services,
#			'past_services':past_services
#			})


def product_edit( request, product_form,  product, url):
	category_formset = CategoryClassificationFormSet( instance=product, prefix="categories")
	supplier_formset =SupplierFormSet( instance=product, prefix="supplier")
	return render_form_to_response(request, url,
				       product_context( product_form, category_formset, supplier_formset))

@login_required
def good_edit( request, good_id):
	good = get_object_or_404(Good, pk=good_id)
	good_form = GoodForm(instance=good) 
	return product_edit( request, good_form, good, 'products/goods/form.html')

#@login_required
#def service_edit( request, service_id):
#	service = get_object_or_404(Service, pk=service_id)
#	service_form = ServiceForm(instance=service) 
#	return product_edit( request, service_form, service, 'products/services/form.html')

def product_add( request, url, product_form, product):
	category_formset = CategoryClassificationFormSet( instance=product, prefix="categories")
	supplier_formset =SupplierFormSet( instance=product, prefix="supplier")
	return render_form_to_response(request, url,product_context( product_form, category_formset, supplier_formset))

@login_required
def good_add( request ) :
	good_form = GoodForm() 
	good = Good()
	return product_add( request, 'products/goods/form.html', good_form, good)

@login_required
def service_add( request ) :
	service_form = ServiceForm() 
	service = Service()
	return product_add( request, 'products/services/form.html', service_form, service)

def product_save(request, form, product, list_url, form_url):
	if form.is_valid():
		new_product = form.save( commit=False)
		category_formset = CategoryClassificationFormSet( request.POST, instance=new_product, prefix="categories")
		supplier_formset = SupplierFormSet( request.POST, instance=new_product, prefix="supplier")
		if category_formset.is_valid() and supplier_formset.is_valid():
			new_product.save()
			category_formset.save()
			supplier_formset.save()
			return redirect(to=list_url)
		else:
			new_product.save()
			return render_form_to_repsonse( request, form_url, product_context( form, category_formset, supplier_formset))
	else:
		category_formset = CategoryClassificationFormSet( instance=product, prefix="categories")
		supplier_formset =SupplierFormSet( instance=product, prefix="supplier")
		return render_form_to_response(request, form_url, product_context(good_form, category_formset, supplier_formset))
@login_required
def good_save( request) :
	good_form = GoodForm( request.POST )
	return product_save(request, good_form, Good(), '/products/goods', 'products/goods/form.html')

@login_required
def service_save( request) :
	service_form = ServiceForm( request.POST )
	return product_save(request, service_form, Service(), '/products/services', 'products/services/form.html')

def product_update( request, form_url, list_url, form, product) :
	if form.is_valid():
		category_formset = CategoryClassificationFormSet( request.POST, instance=product, prefix="categories")
		supplier_formset = SupplierFormSet( request.POST, instance=product, prefix="supplier")
		if category_formset.is_valid() and supplier_formset.is_valid():
			product.save()
			category_formset.save()
			supplier_formset.save()
			return redirect(to=list_url)
	return render_form_to_response( request, form_url, product_context( form, category_formset, supplier_formset))

@login_required
def good_update( request, good_id ) :
	if request.method == 'POST':
		good = get_object_or_404(Good, pk=good_id)
		good_form = GoodForm( request.POST, instance=good)
		return product_update( request, 'products/goods/form.html', '/products/goods', good_form, good)

@login_required
def service_update( request, service_id ) :
	if request.method == 'POST':
		service = get_object_or_404(Service, pk=service_id)
		service_form = ServiceForm( request.POST, instance=service)
		return product_update( request, 'products/services/form.html', '/products/goods', service_form, service)

def product_context( product_form, category_formset, supplier_formset):
	return {'product_form': product_form,
		'category_formset':category_formset,
		'supplier_formset':supplier_formset
		}
