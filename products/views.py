from datetime import datetime

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.forms.models import modelformset_factory, inlineformset_factory
from django.db.models import Q

from common.forms import render_form_to_response, make_custom_field
from products.forms import *
from products.models import *

CategoryClassificationFormSet = inlineformset_factory( Good, CategoryClassification, extra=1, formfield_callback=make_custom_field )
SupplierFormSet = inlineformset_factory( Good, SupplierProduct, extra=1, formfield_callback=make_custom_field )

@login_required
def index( request ) :
	return render_to_response('products/index.html', {})

@login_required
def good_index( request ) :
	current_goods = Good.objects.filter( 
			(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
			(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
		)
	future_goods = Good.objects.filter( 
			Q(introduction_date__gte = datetime.now()) 
		)
	past_goods = Good.objects.filter( 
			Q(sales_discontinuation_date__lte=datetime.now()) 
		)
	return render_to_response('products/good_index.html', {
			'current_goods':current_goods, 
			'future_goods':future_goods,
			'past_goods':past_goods
		})

@login_required
def service_index( request ) :
	current_services = Service.objects.filter( 
		(Q(introduction_date__lte = datetime.now()) | Q(introduction_date__isnull=True)) &
		(Q(sales_discontinuation_date__gte=datetime.now()) | Q(sales_discontinuation_date__isnull=True))
		)
	future_services = Service.objects.filter( 
		Q(introduction_date__gte = datetime.now()) 
		)
	past_services = Service.objects.filter( 
		Q(sales_discontinuation_date__lte=datetime.now()) 
		)
	return render_to_response('products/service_index.html', {
			'current_services':current_services, 
			'future_services':future_services,
			'past_services':past_services
			})

@login_required
def good_edit( request, good_id):
	good = get_object_or_404(Good, pk=good_id)
	good_form = GoodForm(instance=good) 
	category_formset = CategoryClassificationFormSet( instance=good, prefix="categories")
	supplier_formset =SupplierFormSet( instance=good, prefix="supplier")
	return render_form_to_response(request, 'products/good_form.html', 
			product_context( good_form, category_formset, supplier_formset))

@login_required
def service_edit( request, service_id):
	service = get_object_or_404(Service, pk=service_id)
	service_form = ServiceForm(instance=good) 
	category_formset = CategoryClassificationFormSet( instance=service, prefix="categories")
	supplier_formset =SupplierFormSet( instance=service, prefix="supplier")
	return render_form_to_response(request, 'products/service_form.html', 
			product_context( service_form, category_formset, supplier_formset))

@login_required
def good_add( request ) :
	good_form = GoodForm() 
	good = Good()
	category_formset = CategoryClassificationFormSet( instance=good, prefix="categories")
	supplier_formset =SupplierFormSet( instance=good, prefix="supplier")
	return render_form_to_response(request, 'products/good_form.html', product_context( good_form, category_formset, supplier_formset))

@login_required
def service_add( request ) :
	service_form = ServiceForm() 
	service = Service()
	category_formset = CategoryClassificationFormSet( instance=service, prefix="categores")
	supplier_formset =SupplierFormSet( instance=service, prefix="supplier")
	return render_form_to_response(request, 'products/service_form.html', product_context( service_form, category_formset, supplier_formset))

@login_required
def good_save( request) :
	if request.method == 'POST':
		good_form = GoodForm( request.POST )
		if good_form.is_valid():
			new_good = good_form.save(commit=False)	
			category_formset = CategoryClassificationFormSet(request.POST, instance=new_good, prefix="categories")
			supplier_formset =SupplierFormSet( request.POST, instance=new_good, prefix="supplier" )
			if category_formset.is_valid() and supplier_formset.is_valid():
				new_good.save()
				category_formset.save()
				supplier_formset.save()
				return redirect(to='/products/goods')
			else:
				new_good.save()
				return render_form_to_response(request, 'products/good_form.html', product_context(good_form, category_formset, supplier_formset))
		else:
			good = Good()
			category_formset = CategoryClassificationFormSet( instance=good, prefix="categories")
			supplier_formset =SupplierFormSet( instance=good, prefix="supplier")
			return render_form_to_response(request, 'products/good_form.html', product_context(good_form, category_formset, supplier_formset))

@login_required
def service_save( request) :
	if request.method == 'POST':
		service_form = ServiceForm( request.POST )
		if service_form.is_valid():
			new_service = service_form.save(commit=False)	
			category_formset = CategoryClassificationFormSet(request.POST, instance=new_service, prefix="categories")
			supplier_formset =SupplierFormSet( request.POST, instance=new_service, prefix="supplier" )
			if category_formset.is_valid() and supplier_formset.is_valid():
				new_service.save()
				category_formset.save()
				supplier_formset.save()
				return redirect(to='/products/services')
			else:
				new_service.save()
				return render_form_to_response(request, 'products/serivce_form.html', product_context(service_form, category_formset, supplier_formset))
		else:
			service = Service()
			category_formset = CategoryClassificationFormSet( instance=service, prefix="categories")
			supplier_formset =SupplierFormSet( instance=service, prefix="supplier")
			return render_form_to_response(request, 'products/service_form.html', product_context(service_form, category_formset, supplier_formset))

@login_required
def good_update( request, good_id ) :
	if request.method == 'POST':
		good = get_object_or_404(Good, pk=good_id)
		good_form = GoodForm( request.POST, instance=good)
		if good_form.is_valid():
			category_formset = CategoryClassificationFormSet(request.POST, instance=good, prefix="categories")
			supplier_formset =SupplierFormSet( request.POST, instance=good, prefix="supplier" )
			if category_formset.is_valid() and supplier_formset.is_valid():
				good.save()
				category_formset.save()
				supplier_formset.save()
				return redirect(to='/products/goods')
	return render_form_to_response(request, 'products/good_form.html', product_context(good_form, category_formset, supplier_formset))

@login_required
def service_update( request, service_id ) :
	if request.method == 'POST':
		service = get_object_or_404(Service, pk=service_id)
		service_form = ServiceForm( request.POST, instance=service)
		if service_form.is_valid():
			category_formset = CategoryClassificationFormSet(request.POST, instance=service, prefix="categories")
			supplier_formset =SupplierFormSet( request.POST, instance=service, prefix="supplier" )
			if category_formset.is_valid() and supplier_formset.is_valid():
				service.save()
				category_formset.save()
				supplier_formset.save()
				return redirect(to='/products/services')
	return render_form_to_response(request, 'products/service_form.html', product_context(good_form, category_formset, supplier_formset))

def product_context( product_form, category_formset, supplier_formset):
	return {'product_form': product_form,
		'category_formset':category_formset,
		'supplier_formset':supplier_formset
		}
