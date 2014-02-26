from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
from django.contrib.auth.decorators import login_required
from views import *
from models import *

urlpatterns = patterns('party.views',
	(r'^$', login_required(ListView.as_view( model=Party ))),
)
