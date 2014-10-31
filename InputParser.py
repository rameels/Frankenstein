import csv
from frankapp.models import Stages, Events, Actors

# with open('Event.csv', 'rb') as f:
#     reader = csv.reader(f, delimiter=',')
#     for row in reader:
# 	
# 		eventcreated = Events(
# 		                      name = row[1],
#                                       description = row[2],
# 		                      duration = row[3],
# 		                      stage_id = row[4])
#                 eventcreated.save()

with open('Stage.csv', 'rb') as f:
    reader = csv.reader(f, delimiter=',')
    reader.next()
    for row in reader:
        stagecreated = Stages(
            name = row[1],
            description = row[2])
        stagecreated.save()
