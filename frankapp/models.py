from django.db import models

# Create your models here.

class Stages(models.Model):
	name = models.CharField(max_length=30)
	description = models.CharField(max_length=100)
	
	def __unicode__(self):
		return self.name

	def getData(self):
		return [self.id, str(self.name), str(self.description)]

class Events(models.Model):
	name = models.CharField(max_length=100)
	description = models.CharField(max_length=300)
	duration = models.IntegerField()
	stage = models.ForeignKey(Stages)
	def __unicode__(self):
		return self.name
	
	def getData(self):
		return [self.id, str(self.name), str(self.description), self.duration, self.stage.id]

	def getBasicData(self):
		return [str(self.name), str(self.description), self.duration, self.stage.id]

class EventsTimes(models.Model):
	daytime = models.DateTimeField(auto_now_add=True)
	event = models.ForeignKey(Events)
	
	def getData(self):
		return [self.id, str(self.daytime), self.event.id]

class Actors(models.Model):
	name = models.CharField(max_length=30)
	def __unicode__(self):
		return self.name
	
	def getData(self):
		return [self.id, str(self.name)]
    
class Roles(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name
	
	def getData(self):
		return [self.id, str(self.name)]
 
class ActorsRoles(models.Model):
	actor = models.ForeignKey(Actors)
	role = models.ForeignKey(Roles)
	eventstimes = models.ForeignKey(EventsTimes, default=1)
	
	def __unicode__(self):
		return self.actor.name + ": " + self.role.name
	
	def getkey(self):
		return self.actor.name

	def getvalue(self):
		return [self.role.name,self.eventstimes.event.name,self.eventstimes.event.stage.name,str(self.eventstimes.daytime)]
    
	def getData(self):
		return [self.id, self.actor.id, self.role.id, self.eventstimes.id]
    
class Crew(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name
	
	def getData(self):
		return [self.id, str(self.name)]
    
class Responsibilities(models.Model):
	name = models.CharField(max_length=30)
	
	def __unicode__(self):
		return self.name
	
	def getData(self):
		return [self.id, str(self.name)]
 
class CrewResponsibilities(models.Model):
	crew = models.ForeignKey(Crew)
	responsibility = models.ForeignKey(Responsibilities)
	stage = models.ForeignKey(Stages)
	
	def __unicode__(self):
		return self.crew.name + ": " + self.responsibility.name + ", " + self.stage.name
	
	def getkey(self):
		return self.crew.name
    
	def getvalue(self):
		return [self.responsibility.name,self.stage.name]
    
	def getData(self):
		return [self.id, self.crew.id, self.responsibility.id, self.stage.id]
