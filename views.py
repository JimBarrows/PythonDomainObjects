from django.forms import ModelForm, DateField
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.forms import ModelForm, DateField
from django.http import HttpResponse
from django.template import Context, loader
from django.shortcuts import render_to_response, redirect
from django.core.context_processors import csrf
from django.contrib.auth.decorators import login_required
from party.models import Organization, PartyRole, PartyRoleType
from common.widgets import DatePickerWidget
from business.views import primaryBusinessFormQuery

@login_required
def index( request):
	if primaryBusinessFormQuery.exists():
		return render_to_response('index.html', {})
	else:
		return redirect(to='business/setup')
		

