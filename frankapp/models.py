from django.db import models

# Create your models here.

class Stages(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	def __unicode__(self):
		return self.name

class Events(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	duration = models.IntegerField()
	stage = models.ForeignKey(Stages)
	def __unicode__(self):
		return self.name

class EventsTimes(models.Model):
	daytime = models.DateTimeField()
	event = models.ForeignKey(Events)

class Actors(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
    
class Roles(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
 
class ActorsRoles(models.Model):
	actor = models.ForeignKey(Actors)
	role = models.ForeignKey(Roles)
	eventstimes = models.ForeignKey(EventsTimes)
##	def __unicode__(self):
##		return self.actor.name + ": " + self.role.name
	def getkey(self):
                return self.actor.name
        def getvalue(self):
                return self.role.name
        def __unicode__(self):
                return getkey(self) + ": " + getvalue(self)
    
class Crew(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
    
class Responsibilities(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
 
class CrewResponsibilities(models.Model):
	crew = models.ForeignKey(Crew)
	responsibility = models.ForeignKey(Responsibilities)
	stage = models.ForeignKey(Stages)
	def __unicode__(self):
		return self.crew.name + ": " + self.responsibility.name + ", " + self.stage.name
