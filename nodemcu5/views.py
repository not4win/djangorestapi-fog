from rest_framework.views import APIView
from rest_framework import viewsets
from .models import nodemcu5
from .serializers import Nodemcu5Serializer
# Create your views here.
class Nodemcu5View(viewsets.ModelViewSet):
	queryset=nodemcu5.objects.all()
	serializer_class=Nodemcu5Serializer

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
