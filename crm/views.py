from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from models import *
from party.models import Person, PartyRole
from common.views import customer_role
from crm.forms import PersonForm

def make_customer( party):
		party_role = PartyRole(party=party,
													 party_role_type=customer_role)
		party_role.save()

class PersonCreate ( CreateView):
	form_class=PersonForm
	template_name='crm/person_form.html'
	success_url='/crm'

	def form_valid(self, form):
		self.object = form.save()
		make_customer( self.object)
		return HttpResponseRedirect(self.get_success_url())

class PersonUpdate ( UpdateView):
	form_class=PersonForm
	model=Person
	template_name='crm/person_form.html'
	success_url='/crm'

	def form_valid(self, form):
		self.object = form.save()
		return HttpResponseRedirect(self.get_success_url())

class PersonDelete ( DeleteView):
	model=Person
	template_name='crm/person_confirm_delete.html'
	success_url='/crm'
