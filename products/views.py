from datetime import datetime
from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from common.forms import render_form_to_response
from django.forms.models import modelformset_factory, inlineformset_factory


from products.forms import GoodForm
from products.models import CategoryClassification, Good, SupplierProduct

CategoryClassificationFormSet = inlineformset_factory( Good, CategoryClassification, extra=1 )
SupplierFormSet = inlineformset_factory( Good, SupplierProduct, extra=1 )

def index( request ) :
	return render_to_response('products/index.html', {})

def good_index( request ) :
	current_goods = Good.objects.filter( introduction_date__lte=datetime.now())#.filter( sales_discontinuation_date__lte=datetime.now())
	return render_to_response('products/good_index.html', {'current_goods':current_goods})

def good_add( request ) :
	good_form = GoodForm() 
	good = Good()
	category_formset = CategoryClassificationFormSet( instance=good, prefix="categories")
	supplier_formset =SupplierFormSet( instance=good, prefix="supplier")
	return render_form_to_response(request, 'products/good_form.html', product_context( good_form, category_formset, supplier_formset))

def good_save( request ) :
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
	return render_form_to_response(request, 'products/good_form.html', product_context(good_form, category_formset, supplier_formset))

def product_context( product_form, category_formset, supplier_formset):
	return {'product_form': product_form,
		'category_formset':category_formset,
		'supplier_formset':supplier_formset
	}
