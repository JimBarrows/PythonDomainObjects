from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from views import *
from models import *
from party.models import Party, Person
from common.views import customer_role
from crm.forms import CustomerForm

urlpatterns = patterns('crm.urls',
	(r'^$', login_required(  ListView.as_view( 
			queryset=Party.objects.filter(partyrole__party_role_type=customer_role), 
			template_name='crm/customer_list.html'))),
	(r'^add_person', login_required( CustomerCreate.as_view())),
	(r'^update/(?P<pk>\d+)', login_required( CustomerUpdate.as_view())),
	(r'^delete/(?P<pk>\d+)', login_required( CustomerDelete.as_view())),
	(r'^(?P<pk>\d+)$', login_required(  DetailView.as_view( 
			model=Party, 
			template_name='crm/person_detail.html'))),
)
