from rest_framework import serializers
from .models import iotdevices

class FluxgenSerializer(serializers.ModelSerializer):
	class Meta:
		model = iotdevices
		fields=('id','device_id','time','temparature','pressure')