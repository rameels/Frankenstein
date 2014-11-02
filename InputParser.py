import csv
from frankapp.models import Stages, Events, EventsTimes, Actors, Roles, ActorsRoles, Crew, Responsibilities, CrewResponsibilities

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
