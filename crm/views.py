from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponseRedirect
from models import *
from party.models import Person, PartyRole
from common.views import customer_role
from crm.forms import PersonForm

class PersonCreate ( CreateView):
	form_class=PersonForm
	template_name='crm/person_form.html'
	success_url='/crm'

	def form_valid(self, form):
		self.object = form.save()
		print("object: {0}".format(self.object))
		party_role = PartyRole(party=self.object,
													 party_role_type=customer_role)
		party_role.save()
		return HttpResponseRedirect(self.get_success_url())
