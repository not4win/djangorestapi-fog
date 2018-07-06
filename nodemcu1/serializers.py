from rest_framework import serializers
from .models import nodemcu1

class Nodemcu1Serializer(serializers.ModelSerializer):
	class Meta:
		model = nodemcu1
		fields=('id','time','temparature','pressure')