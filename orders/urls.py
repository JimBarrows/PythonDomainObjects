from django.conf.urls.defaults import *
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from views import *
from models import *

urlpatterns = patterns('orders.views',
	(r'^sales$', login_required(ListView.as_view( model=SalesOrder ))),
)
