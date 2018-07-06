from rest_framework import serializers
from .models import nodemcu3

class Nodemcu3Serializer(serializers.ModelSerializer):
	class Meta:
		model = nodemcu3
		fields=('id','time','temparature','pressure')