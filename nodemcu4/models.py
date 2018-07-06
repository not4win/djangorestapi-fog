from django.db import models

# Create your models here.
class nodemcu4(models.Model):
	time=models.CharField(max_length=50,default='null')
	temparature=models.CharField(max_length=50,default='null')
	pressure=models.CharField(max_length=50,default='null')

	def __str__(self):
		return self.time