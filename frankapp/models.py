from django.db import models

# Create your models here.

class Stages(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)

class Events(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	duration = models.IntegerField()
	stage_id = models.ForeignKey(Stages)

class EventsTimes(models.Model):
	daytime = models.DateTimeField()
	event = models.ForeignKey(Events)
 
class Actors(models.Model):
	name = models.CharField(max_length=30)
    
class Roles(models.Model):
	name = models.CharField(max_length=30)
 
class ActorsRoles(models.Model):
	actor = models.ForeignKey(Actors)
	role = models.ForeignKey(Roles)
	stage = models.ForeignKey(Stages)
    
class Crew(models.Model):
	name = models.CharField(max_length=30)
    
class Responsibilities(models.Model):
	name = models.CharField(max_length=30)
 
class CrewResponsibilities(models.Model):
	crew = models.ForeignKey(Crew)
	responsibility = models.ForeignKey(Responsibilities)
	stage = models.ForeignKey(Stages)
