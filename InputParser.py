import csv
from frankapp.models import Stages, Events, Roles

with open('Stage.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        stagecreated, create = Stages.objects.get_or_create(
            id = row[0],
            name = row[1],
            description = row[2])
        if (create):
            stagecreated.save()
            print "new Stages tuble created"

with open('Event.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        eventcreated, create = Events.objects.get_or_create(
            id = row[0], 
            name = row[1],
            description = row[2],
            duration = row[3],
            stage_id = Stages.objects.get(id = row[4]).id)
        if (create):
            eventcreated.save()
            print "new Events tuble created"

with open('Role.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        rolecreated, create = Roles.objects.get_or_create(
            id = row[0],
            name = row[1])
        if (create):
            rolecreated.save()
            print "new Roles tuble created"
