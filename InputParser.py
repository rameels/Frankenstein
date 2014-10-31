import csv

from frankapp.models import Events
#from django.db import models

with open('Event.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    for row in reader:
	
		eventcreated = Events.objects.create(
						name = row[1],
						description = row[2],
						duration = row[3],
						stageid = row[4])
						