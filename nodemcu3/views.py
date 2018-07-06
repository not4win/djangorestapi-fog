from rest_framework.views import APIView
from rest_framework import viewsets
from .models import nodemcu3
from .serializers import Nodemcu3Serializer
# Create your views here.
class Nodemcu3View(viewsets.ModelViewSet):
	queryset=nodemcu3.objects.all()
	serializer_class=Nodemcu3Serializer

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
