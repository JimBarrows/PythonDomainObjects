from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from models import *
from party.models import Party, Person, PartyRole, Organization, PartyClassification
from common.views import customer_role
from crm.forms import CustomerForm

def add_roles( party):
		party_role = PartyRole(party=party,
													 party_role_type=customer_role)
		party_role.save()

class CustomerCreate ( CreateView):
	form_class=CustomerForm
	template_name='crm/customer_form.html'
	success_url='/crm'

	def form_valid(self, form):
		print("Before self.object={0}".format(self.object))
		if( form.cleaned_data['customer_type'] == 'Person') :
			self.object = Person( first_name=form.cleaned_data['first_name'],
														middle_name=form.cleaned_data['middle_name'],
														last_name=form.cleaned_data['last_name'])
			self.object.save()
		else :
			self.object = Organization(name=form.cleaned_data['name'])
			self.object.save()
			PartyClassification(party=self.object,
													party_type = form.cleaned_data['organization_type']).save()
		print("After self.object={0}".format(self.object))
		add_roles( self.object)
		return HttpResponseRedirect(self.get_success_url())

class CustomerUpdate ( UpdateView):
	form_class=CustomerForm
	model=Party
	template_name='crm/customer_form.html'
	success_url='/crm'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

class CustomerDelete ( DeleteView):
	model=Party
	template_name='crm/customer_confirm_delete.html'
	success_url='/crm'
