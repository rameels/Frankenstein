from django.shortcuts import render

from frankapp.models import *

# Create your views here.
def search(request):
	return render(request, 'frankapp/search.html')

def searchpeople(request):
	if 'types' in request.GET:
		types = request.GET['types'])
		if 'actor' in types:
			actor = types['actor']
		if 'crew' in types:

		if 'role' in types:


	return render(request, 'frankapp/search/people.html', {'results_list': results})

def searchevents(request):
	if 'stage' in request.GET:
		results = Stages.objects.filter(name=request.GET['stage'])
	return render(request, 'frankapp/search/events.html', {'results_list': results})