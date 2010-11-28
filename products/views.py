from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from common.forms import render_form_to_response
from django.forms.models import modelformset_factory


from products.forms import GoodForm
from products.models import Category

CategoryFormSet = modelformset_factory( Category, exclude='product')

def index( request ) :
	return render_to_response('products/index.html', {})



def good_add( request ) :
	formset = CategoryFormSet(queryset=Category.objects.none())
	context = {'form':GoodForm(), 
		'category_formset':formset
	}
	return render_form_to_response(request, 'products/good_form.html', context)



def good_save( request ) :
	if request.method == 'POST':
		form = GoodForm( request.POST )
		if form.is_valid():
			form.save()	
	return render_form_to_response(request, 'products/good_form.html', {'form':GoodForm()})
