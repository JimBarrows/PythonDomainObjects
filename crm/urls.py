from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from views import *
from models import *
from party.models import Party
from common.views import customer_role

urlpatterns = patterns('crm.urls',
	(r'^$', login_required(  ListView.as_view( 
			queryset=Party.objects.filter(role__role_type=customer_role), 
			template_name='crm/customer_list.html'))),
	(r'^(?P<pk>\d+)$', login_required(  DetailView.as_view( 
			model=Party, 
			template_name='crm/person_detail.html'))),
)
