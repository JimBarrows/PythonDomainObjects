from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import DateField

from common.forms import render_form_to_response
from common.widgets import DatePickerWidget
from party.models import Organization, PartyRole, PartyRoleType, PartyRelationshipType, PartyRelationship
from business.forms import BusinessForm, SubOrgForm


internalOrganizations = Organization.objects.filter( roles__description__exact='Internal Organization')

primaryBusinessFormQuery = internalOrganizations.filter( roles__description__exact='Parent Organization')

organizationRollup = PartyRelationshipType.objects.filter( name__exact='Organization Rollup').get()

departmentRole = PartyRoleType.objects.filter( description__exact='Department').get()
internalOrgRole = PartyRoleType.objects.filter( description__contains='Internal Organization').get()

@login_required
def index( request):
	c = {
		'form' : SubOrgForm(),
		'business':primaryBusinessFormQuery.get(),
		'departments':internalOrganizations.filter( roles__description__exact='Department'),
		'divisions':internalOrganizations.filter( roles__description__exact='Division'),
		'subsidiarys':internalOrganizations.filter( roles__description__exact='Subsidiary'),
		'dbas':internalOrganizations.filter( roles__description__exact='DBA'),
	}
	c.update(csrf(request))
	return render_to_response('business/index.html', c)

@login_required
def subOrganizationForm( request ) :
	return render_form_to_response(request, 'business/subOrganizationForm.html', {'form' :SubOrgForm()})

@login_required
def add_sub_org( request):
	if request.method =='POST':
		form = SubOrgForm(request.POST)
		if( form.is_valid()):
			primary = primaryBusinessFormQuery.get()

			newDepartment = Organization.objects.create( name=form.cleaned_data['name'])

			PartyRole.objects.create( 
					party_role_type=internalOrgRole, 
					party=newDepartment, 
					from_date=form.cleaned_data['date_started'])
			roleName = form.cleaned_data['sub_org_role']	
			newRole = PartyRole.objects.create( 
					party_role_type=PartyRoleType.objects.filter( description__exact= roleName).get(), 
					party=newDepartment, 
					from_date=form.cleaned_data['date_started'])

			PartyRelationship.objects.create( 
					comment=primary.name + ' -> ' + newDepartment.name,
					relationship_type=organizationRollup, 
					from_date = form.cleaned_data['date_started'],
					from_role = primary.findRoleByName('Parent Organization'),
					to_role = newRole)

	return redirect(to='/business')

@login_required
def setup( request):
	if request.method == 'POST':
		form = BusinessForm(request.POST)
		if form.is_valid():
			if primaryBusinessFormQuery.exists():
				organization = primaryBusinessFormQuery.get()
				organization.name = form.cleaned_data['name']
				role = organization.findRoleByName('Internal Organization')
				role.from_date=form.cleaned_data['date_started']
				role.save()
				role = organization.findRoleByName('Parent Organization')
				role.from_date=form.cleaned_data['date_started']
				role.save()
				organization.roles.filter( description__exact='Parent Organization').get().from_date=form.cleaned_data['date_started']
				organization.save()
			else:
				organization = Organization.objects.create( name=form.cleaned_data['name'])
				parentRole = PartyRoleType.objects.filter( description__contains='Parent Organization').get()
				PartyRole.objects.create( party=organization, party_role_type=internalOrgRole, from_date=form.cleaned_data['date_started'])
				PartyRole.objects.create( party=organization, party_role_type=parentRole, from_date=form.cleaned_data['date_started'] )
	else:
		if( primaryBusinessFormQuery.exists()):
			organization = primaryBusinessFormQuery.get()	
			role = organization.findRoleByName('Internal Organization')
			form = BusinessForm({ 'name' : organization.name, 'date_started' : role.from_date})
		else:
			form = BusinessForm()
	c = {'form':form}
	c.update(csrf(request))
	return render_form_to_response(request, 'business/setup/index.html', c)

def thisIsATest():
	return "This is a test"
