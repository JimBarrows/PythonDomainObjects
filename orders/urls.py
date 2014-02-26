from django.conf.urls import patterns, url
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from views import *
from models import SalesOrder

urlpatterns = patterns('orders.views',
					url(r'^sales$', login_required(ListView.as_view( model=SalesOrder ))),
)
