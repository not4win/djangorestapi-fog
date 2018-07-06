from rest_framework import serializers
from .models import nodemcu5

class Nodemcu5Serializer(serializers.ModelSerializer):
	class Meta:
		model = nodemcu5
		fields=('id','time','temparature','pressure')