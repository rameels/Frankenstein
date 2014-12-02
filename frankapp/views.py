import json, urllib
from django.shortcuts import render
from django.http import HttpResponse
from frankapp.models import *
from datetime import datetime
from django.utils import timezone

# Create your views here.
def index(request):
    return render(request, 'frankapp/index.html')

def updatedb(request):
    print request.POST
    print 'hey!'

def getdatafromdb(request):
    results = {}

##    allType = ['stages','events','eventstimes','actors','roles','actorsroles','crew','responsibilities','crewResponsibilities']
    allOptions = {'__stages__' : returnStages(''),
                  '__events__' : returnEvents(''),
                  '__eventstimes__' : searchEvents(''),
                  '__actors__' : returnActors(''),
                  '__roles__' : returnRoles(''),
                  '__actorsroles__' : searchActor(''),
                  '__crew__' : returnCrew(''),
                  '__responsibilities__' : returnResp(''),
                  '__crewResponsibilities__' : searchCrew(''),
}
    allType = allOptions.keys()
    print allType

    
    if 'types' in request.GET:
        types = request.GET['types']
        if 'all' in types:
            types = allType
        elif 'mangoevents' in types:
            results = mangoevents('')
            
        for typename in allType:
            if typename in types:
                results[typename] = toDict(allOptions[typename])
        
    return HttpResponse(json.dumps(results), content_type="application/json")

def searchpeople(request):
    android = False
    name = ''
    
    if 'android' in request.GET:
        if 'true' in request.GET['android']:
            android = True
            
    if 'types' in request.GET:
        types = request.GET['types']
        name = request.GET.get('name')
        stringValue = ''
        results = []
        if 'actor' in types:
            stringValue = 'actors_results'
            if 'startDate' and 'endDate' in request.GET:
                start_datetime,end_datetime = convertTime(request)
                results = searchActorTime(start_datetime, end_datetime, name)
            else:
                results = searchActor(name)

        elif 'crew' in types:
            stringValue = 'crew_results'
            results = searchCrew(name)

        elif 'role' in types:
            stringValue = 'role_results'
            results = searchRole(name)
            
    if android == False:
        return render(request, 'frankapp/people.html', {stringValue : results})
    else:
        return HttpResponse(json.dumps(resultsToDict(results)), content_type="application/json")
    
def searchevents(request):
    android = False
    name = ''
    results = []
    if 'android' in request.GET:
        if 'true' in request.GET['android']:
            android = True

    if 'name' in request.GET:
        name = request.GET.get('name')
        
    if 'startDate' and 'endDate' in request.GET:
        start_datetime,end_datetime = convertTime(request)
        results = searchEventsTime(start_datetime, end_datetime, name)
    else:
        results = searchEvents(name)

    if android == False:
        return render(request, 'frankapp/events.html', {'results' : results})
    else:
        return HttpResponse(json.dumps(resultsToDict(results)), content_type="application/json")

def mangoevents(name):

    eventstimelist = searchEvents(name)

    resultsdict = {}

    for eventtime in eventstimelist:
        resultsdict[eventtime.id] = eventtime.event.getBasicData()

        resultsdict[eventtime.id].append(str(eventtime.daytime))

        actorsroleslist = searchActorRoleByEventTime(eventtime.id)
        actorsrolesidlist = []

        for actorrole in actorsroleslist:
            actorsrolesidlist.append({'actor_id':actorrole.actor.id, 'role_id':actorrole.role.id})
        
        resultsdict[eventtime.id].append(actorsrolesidlist)

    return resultsdict

# search methods begin. search*** is for the relations, and return*** for the rest

def toDict(results):
    totalResults = []
    for d in results:
        totalResults.append(d.getData())
    return totalResults

def returnStages(name):
    return Stages.objects.filter(name__contains=name)

def returnEvents(name):
    return Events.objects.filter(name__contains=name)

def searchEvents(name):
    return EventsTimes.objects.filter(event__name__contains=name)

def searchEventsTime(start_datetime,end_datetime,name):
    return EventsTimes.objects.filter(event__name__contains=name, daytime__gte=start_datetime, daytime__lte=end_datetime)

def returnActors(name):
    return Actors.objects.filter(name__contains=name)

def returnRoles(name):
    return Roles.objects.filter(name__contains=name)

def returnCrew(name):
    return Crew.objects.filter(name__contains=name)

def returnResp(name):
    return Responsibilities.objects.filter(name__contains=name)

def searchCrew(name):
    return CrewResponsibilities.objects.filter(crew__name__contains=name)

def searchRole(name):
    return ActorsRoles.objects.filter(role__name__contains=name)

def searchActor(name):
    return ActorsRoles.objects.filter(actor__name__contains=name)

def searchActorTime(start_datetime, end_datetime, name):
    return ActorsRoles.objects.filter(actor__name__contains=name, eventstimes__daytime__gte=start_datetime, eventstimes__daytime__lte=end_datetime)

def searchActorRoleByEventTime(et_id):
    return ActorsRoles.objects.filter(eventstimes__id = et_id)

# Search methods end


def convertTime(request):
    start_date = urllib.unquote(request.GET.get('startDate')).decode('utf8').split('/')
    start_datetime = datetime(int(start_date[2]), int(start_date[0]), int(start_date[1]),0,0)
    end_date = urllib.unquote(request.GET.get('endDate')).decode('utf8').split('/')
    end_datetime = datetime(int(end_date[2]), int(end_date[0]), int(end_date[1]),0,0)
    return start_datetime, end_datetime

def resultsToDict(results):
    response_data = {}
    
    for result in results:
        
        if (result.getkey() not in response_data):
            response_data[result.getkey()] = [result.getvalue()]
        else:
            response_data[result.getkey()].append(result.getvalue())
            
    return response_data
