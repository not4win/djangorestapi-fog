from rest_framework import serializers
from .models import nodemcu4

class Nodemcu4Serializer(serializers.ModelSerializer):
	class Meta:
		model = nodemcu4
		fields=('id','time','temparature','pressure')