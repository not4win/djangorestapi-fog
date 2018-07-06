from rest_framework.views import APIView
from rest_framework import viewsets
from .models import nodemcu2
from .serializers import Nodemcu2Serializer
# Create your views here.
class Nodemcu2View(viewsets.ModelViewSet):
	queryset=nodemcu2.objects.all()
	serializer_class=Nodemcu2Serializer

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
