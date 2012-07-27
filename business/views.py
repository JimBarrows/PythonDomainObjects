from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from django.forms import DateField
from django.views.generic import CreateView, UpdateView
from django.http import HttpResponseRedirect

from common.forms import render_form_to_response
from common.views import *
from common.widgets import DatePickerWidget
from party.models import Organization, PartyRole, PartyRoleType, PartyRelationshipType, PartyRelationship
from business.forms import BusinessForm, SubOrgForm



class BusinessCreate( CreateView):
	model=Organization	
	form_class=BusinessForm
	success_url='business/setup/index.html'

	def form_valid(self, form):
		self.object = form.save()
		PartyRole.objects.create( party=self.object, party_role_type=internalOrgRole, from_date=form.cleaned_data['date_started'])
		PartyRole.objects.create( party=self.object, party_role_type=parentRole, from_date=form.cleaned_data['date_started'] )
		return HttpResponseRedirect(self.get_success_url())
			

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

