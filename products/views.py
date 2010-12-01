from django.http import HttpResponse
from django.shortcuts import render_to_response, redirect
from common.forms import render_form_to_response
from django.forms.models import modelformset_factory, inlineformset_factory


from products.forms import GoodForm
from products.models import CategoryClassification, Good

CategoryClassificationFormSet = inlineformset_factory( Good, CategoryClassification, extra=1 )

def index( request ) :
	return render_to_response('products/index.html', {})



def good_add( request ) :
	good_form = GoodForm() 
	good = Good()
	formset = CategoryClassificationFormSet( instance=good)
	context = {'form': good_form,
		'category_formset':formset
	}
	return render_form_to_response(request, 'products/good_form.html', context)



def good_save( request ) :
	if request.method == 'POST':
		good_form = GoodForm( request.POST )
		if good_form.is_valid():
			new_good = good_form.save(commit=False)	
			category_classification_formset = CategoryClassificationFormSet(request.POST, instance=new_good)
			if category_classification_formset.is_valid():
				new_good.save()
				category_classification_formset.save()
				return redirect(to='/products')
	return render_form_to_response(request, 'products/good_form.html', {'form':form, 'category_formset': category_classifciation_formset})

