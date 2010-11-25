from django import forms
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from party.models import Organization, PartyRole, PartyRoleType

def index( request):
	''' does nothing '''

def setup( request):
	if request.method == 'POST':
		form = Business(request.POST)
		if form.is_valid():
			organization = Organization.objects.create( name=form.cleaned_data['name'])
			internalOrgRole = PartyRoleType.objects.filter( description__contains='Internal Organization').get()
			parentRole = PartyRoleType.objects.filter( description__contains='Parent Organization').get()
			PartyRole.objects.create( party=organization, partyRoleType=internalOrgRole)
			PartyRole.objects.create( party=organization, partyRoleType=parentRole )
	else:
		form = Business()
	c = {'form':form}
	c.update(csrf(request))
	return render_to_response('business/setup/index.html', c)

class Business( forms.Form ):
	name = forms.CharField( max_length=100)
