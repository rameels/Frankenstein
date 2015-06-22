import csv
from frankapp.models import Stages, Events, EventsTimes, Actors, Roles, ActorsRoles, Crew, Responsibilities, CrewResponsibilities
from datetime import datetime
from django.utils import timezone
import django
django.setup()

with open('Stage.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            stagecreated, create = Stages.objects.get_or_create(
                id = row[0],
                name = row[1],
                description = row[2])
            if (create):
                stagecreated.save()
                print "new Stages tuple created"
        except:
            print row
            raise

with open('Event.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            eventcreated, create = Events.objects.get_or_create(
                id = row[0], 
                name = row[1],
                description = row[2],
                duration = row[3],
                stage = Stages.objects.get(id = row[4]))
            if (create):
                eventcreated.save()
                print "new Events tuple created"
        except:
            print row
            raise
            
with open('Role.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            rolecreated, create = Roles.objects.get_or_create(
                id = row[0],
                name = row[1])
            if (create):
                rolecreated.save()
                print "new Roles tuple created"
        except:
            print row
            raise

with open('Crew.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            crewcreated, create = Crew.objects.get_or_create(
                id = row[0],
                name = row[1])
            if (create):
                crewcreated.save()
                print "new Crew tuple created"
        except:
            print row
            raise

with open('Resps.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            respscreated, create = Responsibilities.objects.get_or_create(
                id = row[0],
                name = row[1])
            if (create):
                respscreated.save()
                print "new Responsibilities tuple created"
        except:
            print row
            raise

with open('CrewResps.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            cresp_created, create = CrewResponsibilities.objects.get_or_create(
                crew = Crew.objects.get(id = row[0]),
                responsibility = Responsibilities.objects.get(id = row[1]),
                stage = Stages.objects.get(id = row[2]))
            if (create):
                cresp_created.save()
                print "new CrewResponsibilities tuple created"
        except:
            print row
            raise
            
with open('Eventstimes.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            evtmcreated, create = EventsTimes.objects.get_or_create(
                id = row[0],
                daytime = datetime(int(row[1]),int(row[2]),int(row[3]),int(row[4]),int(row[5])),
                event = Events.objects.get(id = row[6]))
            if (create):
                evtmcreated.save()
                print "new Eventstimes tuple created"
        except:
            print row
            raise

with open('Actor.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            actorcreated, create = Actors.objects.get_or_create(
                id = row[0],
                name = row[1])
            if (create):
                actorcreated.save()
                print "new Actor tuple created"
        except:
            print row
            raise

with open('ActorsRoles.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        try:
            actrl_created, create = ActorsRoles.objects.get_or_create(
                actor = Actors.objects.get(id = row[0]),
                role = Roles.objects.get(id = row[1]),
                eventstimes = EventsTimes.objects.get(id = row[2]))
            if (create):
                actrl_created.save()
                print "new ActorsRoles tuple created"
        except:
            print row
            raise
