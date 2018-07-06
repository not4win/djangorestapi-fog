from rest_framework.views import APIView
from rest_framework import viewsets
from .models import nodemcu4
from .serializers import Nodemcu4Serializer
# Create your views here.
class Nodemcu4View(viewsets.ModelViewSet):
	queryset=nodemcu4.objects.all()
	serializer_class=Nodemcu4Serializer

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
