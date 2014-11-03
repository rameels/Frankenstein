from django.shortcuts import render

from frankapp.models import *

# Create your views here.
def index(request):
    return render(request, 'frankapp/index.html')

def searchpeople(request):
    android = True
    if 'android' in request.GET:
        print "yeah?"
    if 'types' in request.GET:
        types = request.GET['types']
        print request.GET.get('name')
        if 'actor' in types:
            results = ActorsRoles.objects.filter(actor__name=request.GET.get('name'))
        #if 'crew' in types:
        #crew = types['crew']
        #if 'role' in types:
        #role = types['role']
        for result in results:
            print result.actor.name + ": " + result.role.name
    return render(request, 'frankapp/people.html', {'results': results})

def searchevents(request):
    results_list = []
    if 'types' in request.GET:
        types = request.GET['types']
        if 'actor' in types:
            actor = types['actor']
        if 'crew' in types:
            crew = types['crew']
        if 'role' in types:
            role = types['role']
    return render(request, 'frankapp/events.html', {'results_list': results})
