from rest_framework import serializers
from .models import nodemcu2

class Nodemcu2Serializer(serializers.ModelSerializer):
	class Meta:
		model = nodemcu2
		fields=('id','time','temparature','pressure')