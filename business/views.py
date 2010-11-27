from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from common.forms import CommonModelForm
from django.forms import DateField
from common.widgets import DatePickerWidget
from party.models import Organization, PartyRole, PartyRoleType, PartyRelationshipType, PartyRelationship
from business.forms import BusinessForm, SubOrgForm

internalOrganizations = Organization.objects.filter( roles__description__exact='Internal Organization')

primaryBusinessFormQuery = internalOrganizations.filter( roles__description__exact='Parent Organization')

organizationRollup = PartyRelationshipType.objects.filter( name__exact='Organization Rollup').get()

departmentRole = PartyRoleType.objects.filter( description__exact='Department').get()
internalOrgRole = PartyRoleType.objects.filter( description__contains='Internal Organization').get()

def index( request):
	c = {
		'form' : SubOrgForm(),
		'business':primaryBusinessFormQuery.get(),
		'departments':internalOrganizations.filter( roles__description__exact='Department').iterator(),
		'divisions':internalOrganizations.filter( roles__description__exact='Division'),
		'subsidiarys':internalOrganizations.filter( roles__description__exact='Subsidiary'),
		'dbas':internalOrganizations.filter( roles__description__exact='DBA'),
	}
	c.update(csrf(request))
	return render_to_response('business/index.html', c)

def addSubOrg( request):
	if request.method =='POST':
		form = SubOrgForm(request.POST)
		if( form.is_valid()):
			primary = primaryBusinessFormQuery.get()

			newDepartment = Organization.objects.create( name=form.cleaned_data['name'])

			PartyRole.objects.create( 
					partyRoleType=internalOrgRole, 
					party=newDepartment, 
					fromDate=form.cleaned_data['dateStarted'])
			roleName = form.cleaned_data['subOrgRole']	
			newRole = PartyRole.objects.create( 
					partyRoleType=PartyRoleType.objects.filter( description__exact= roleName).get(), 
					party=newDepartment, 
					fromDate=form.cleaned_data['dateStarted'])

			PartyRelationship.objects.create( 
					comment=primary.name + ' -> ' + newDepartment.name,
					relationshipType=organizationRollup, 
					fromDate = form.cleaned_data['dateStarted'],
					fromRole = primary.findRoleByName('Parent Organization'),
					toRole = newRole)

	return redirect(to='/business')

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

