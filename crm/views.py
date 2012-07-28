from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from models import *
from party.models import Party, Person, PartyRole
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
		self.object = form.save()
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
