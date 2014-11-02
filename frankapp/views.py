from django.shortcuts import render

from frankapp.models import Stages

# Create your views here.
def index(request):
	return render(request, 'frankapp/index.html')

def results(request):
	if 'stage' in request.GET:
		results = Stages.objects.filter(name=request.GET['stage'])
	return render(request, 'frankapp/results.html', {'results_list': results})
