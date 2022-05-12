from django.db import models

# Create your models here.

class Album(models.Model):
    name = models.CharField(max_length=30, null=False, blank=False)
    
    def __str__(self):
    	return self.name

class Picture(models.Model):
	album = models.ForeignKey(Album, blank=True, null=True, on_delete=models.SET_NULL)
	image = models.ImageField(null=False, blank=False)
	about = models.CharField(max_length=200, null=False, blank=False)

	def __str__(self):
		return self.about