from django.db import models

# Create your models here.
class iotdevices(models.Model):
	device_id=models.CharField(max_length=50,default='null')
	time=models.CharField(max_length=50,default='null')
	temparature=models.CharField(max_length=50,default='null')
	pressure=models.CharField(max_length=50,default='null')

	def __str__(self):
		return self.device_id