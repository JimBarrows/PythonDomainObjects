from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
#from business.views import primaryBusinessFormQuery

@login_required
def index( request):
	#if primaryBusinessFormQuery.exists():
		return render_to_response('index.html', {}, context_instance=RequestContext(request))
	#else:
	#	return redirect(to='business/setup')
		

