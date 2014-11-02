from django.shortcuts import render

from frankapp.models import *

# Create your views here.
def search(request):
	return render(request, 'frankapp/search.html')

def searchpeople(request):
	if 'stage' in request.GET:
		results = Stages.objects.filter(name=request.GET['stage'])
	return render(request, 'frankapp/searchpeople.html', {'results_list': results})

def searchevents(request):
	if 'stage' in request.GET:
		results = Stages.objects.filter(name=request.GET['stage'])
	return render(request, 'frankapp/searchevents.html', {'results_list': results})