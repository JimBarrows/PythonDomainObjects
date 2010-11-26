from django.forms import ModelForm, DateField
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from party.models import Organization, PartyRole, PartyRoleType
from common.widgets import DatePickerWidget

def index( request):
	''' does nothing '''

primaryBusinessFormQuery =Organization.objects.filter( roles__description__exact='Internal Organization').filter( roles__description__exact='Parent Organization')

def setup( request):
	if request.method == 'POST':
		form = BusinessForm(request.POST)
		if form.is_valid():
			if primaryBusinessFormQuery.exists():
				organization = primaryBusinessFormQuery.get()
				organization.name = form.cleaned_data['name']
				organization.save()
			else:
				organization = Organization.objects.create( name=form.cleaned_data['name'])
				internalOrgRole = PartyRoleType.objects.filter( description__contains='Internal Organization').get()
				parentRole = PartyRoleType.objects.filter( description__contains='Parent Organization').get()
				PartyRole.objects.create( party=organization, partyRoleType=internalOrgRole)
				PartyRole.objects.create( party=organization, partyRoleType=parentRole )
	else:
		if( primaryBusinessFormQuery.exists()):
			organization = primaryBusinessFormQuery.get()	
			form = BusinessForm({ 'name' : organization.name})
		else:
			form = BusinessForm()
	c = {'form':form}
	c.update(csrf(request))
	return render_to_response('business/setup/index.html', c)

class BusinessForm( ModelForm ):
	dateStarted = DateField(label='Date Started', widget=DatePickerWidget)
	class Meta:
		model=Organization
		fields=['name']
