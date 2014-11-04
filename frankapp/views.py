import json, urllib
from django.shortcuts import render
from django.http import HttpResponse
from frankapp.models import *
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'frankapp/index.html')

def searchpeople(request):
    android = False
    actors_results = []
    crew_results = []
    role_results = []
    if 'android' in request.GET:
        if 'true' in request.GET['android']:
            android = True
            
    if 'types' in request.GET:
        types = request.GET['types']
        if 'name' in request.GET:
            name = request.GET.get('name')
        if 'actor' in types:
            if 'startDate' and 'endDate' in request.GET:
                start_date = urllib.unquote(request.GET.get('startDate')).decode('utf8').split('/')
                start_datetime = datetime(int(start_date[2]), int(start_date[0]), int(start_date[1]),0,0)
                end_date = urllib.unquote(request.GET.get('endDate')).decode('utf8').split('/')
                end_datetime = datetime(int(end_date[2]), int(end_date[0]), int(end_date[1]),0,0)
                results = ActorsRoles.objects.filter(actor__name__contains=name, eventstimes__daytime__gte=start_datetime, eventstimes__daytime__lte=end_datetime)
            else:
                results = ActorsRoles.objects.filter(actor__name__contains=name)
            actors_results = results
            resultsdict = {'actors_results' : actors_results}
        elif 'crew' in types:
            results = CrewResponsibilities.objects.filter(crew__name__contains=name)
            crew_results = results
            resultsdict = {'crew_results' : crew_results}
        elif 'role' in types:
            results = ActorsRoles.objects.filter(role__name__contains=name)
            role_results = results
            resultsdict = {'role_results' : role_results}
        print str(results)
    if android == False:
        print resultsdict
        return render(request, 'frankapp/people.html', resultsdict)
    else:
        print "should return json"
        print resultsToDict(results)
        return HttpResponse(json.dumps(resultsToDict(results)), content_type="application/json")
    
def searchevents(request):
    android = False
    results = []
    if 'android' in request.GET:
        if 'true' in request.GET['android']:
            android = True
        if 'name' in request.GET:
            name = request.GET.get('name')
        if 'startDate' and 'endDate' in request.GET:
            start_date = urllib.unquote(request.GET.get('startDate')).decode('utf8').split('/')
            start_datetime = datetime(int(start_date[2]), int(start_date[0]), int(start_date[1]),0,0)
            end_date = urllib.unquote(request.GET.get('endDate')).decode('utf8').split('/')
            end_datetime = datetime(int(end_date[2]), int(end_date[0]), int(end_date[1]),0,0)
            results = EventsTimes.objects.filter(event__name__contains=name, daytime__gte=start_datetime, daytime__lte=end_datetime)
        else:
            results = EventsTimes.objects.filter(event__name__contains=name)
        resultsdict = {'results' : results}
        print str(results)
    if android == False:
        print resultsdict
        return render(request, 'frankapp/events.html', resultsdict)
    else:
        print "should return json"
        print resultsToDict(results)
        return HttpResponse(json.dumps(resultsToDict(results)), content_type="application/json")

def resultsToDict(results):
    response_data = {}
    
    for result in results:
        
        if (result.getkey() not in response_data):
            response_data[result.getkey()] = [result.getvalue()]
        else:
            response_data[result.getkey()].append(result.getvalue())
            
    return response_data
