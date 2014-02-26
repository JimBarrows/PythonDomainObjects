from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from django.contrib.auth.decorators import login_required
from views import CustomerCreate, CustomerUpdate, CustomerDelete
from models import *
from party.models import Party, Person
#from common.views import customer_role
from crm.forms import CustomerForm

urlpatterns = patterns('crm.urls',
					url(r'^$', login_required(  ListView.as_view( 
															#queryset=Party.objects.filter(partyrole__party_role_type=customer_role), 
															template_name='crm/customer_list.html'))),
					url(r'^add', login_required( CustomerCreate.as_view())),
					url(r'^update/(?P<pk>\d+)', login_required( CustomerUpdate.as_view())),
					url(r'^delete/(?P<pk>\d+)', login_required( CustomerDelete.as_view())),
					url(r'^(?P<pk>\d+)$', login_required(  DetailView.as_view( 
																		model=Party, 
																		template_name='crm/customer_detail.html'))),
)
