from rest_framework.views import APIView
from rest_framework import viewsets
from .models import iotdevices
from .serializers import FluxgenSerializer
# Create your views here.
class FluxgenView(viewsets.ModelViewSet):
	queryset=iotdevices.objects.all()
	serializer_class=FluxgenSerializer

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
