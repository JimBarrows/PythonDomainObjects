from django.forms import DateField
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from party.models import Organization, PartyRole, PartyRoleType
from common.widgets import DatePickerWidget
from common.forms import CommonModelForm

internalOrganizations = Organization.objects.filter( roles__description__exact='Internal Organization')

primaryBusinessFormQuery = internalOrganizations.filter( roles__description__exact='Parent Organization')

def index( request):
	c = {
		'business':primaryBusinessFormQuery.get(),
		'departments':internalOrganizations.filter( roles__description__exact='Department')
	}
	return render_to_response('business/index.html', c)

def setup( request):
	if request.method == 'POST':
		form = BusinessForm(request.POST)
		if form.is_valid():
			if primaryBusinessFormQuery.exists():
				organization = primaryBusinessFormQuery.get()
				organization.name = form.cleaned_data['name']
				role = organization.findRoleByName('Internal Organization')
				role.fromDate=form.cleaned_data['dateStarted']
				role.save()
				role = organization.findRoleByName('Parent Organization')
				role.fromDate=form.cleaned_data['dateStarted']
				role.save()
				organization.roles.filter( description__exact='Parent Organization').get().fromDate=form.cleaned_data['dateStarted']
				organization.save()
			else:
				organization = Organization.objects.create( name=form.cleaned_data['name'])
				internalOrgRole = PartyRoleType.objects.filter( description__contains='Internal Organization').get()
				parentRole = PartyRoleType.objects.filter( description__contains='Parent Organization').get()
				PartyRole.objects.create( party=organization, partyRoleType=internalOrgRole, fromDate=form.cleaned_data['dateStarted'])
				PartyRole.objects.create( party=organization, partyRoleType=parentRole, fromDate=form.cleaned_data['dateStarted'] )
	else:
		if( primaryBusinessFormQuery.exists()):
			organization = primaryBusinessFormQuery.get()	
			role = organization.findRoleByName('Internal Organization')
			form = BusinessForm({ 'name' : organization.name, 'dateStarted' : role.fromDate})
		else:
			form = BusinessForm()
	c = {'form':form}
	c.update(csrf(request))
	return render_to_response('business/setup/index.html', c)

class BusinessForm( CommonModelForm ):

	dateStarted = DateField(label='Date Started', widget=DatePickerWidget)
	class Meta:
		model=Organization
		fields=['name']
