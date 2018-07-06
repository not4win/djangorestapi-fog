from rest_framework.views import APIView
from rest_framework import viewsets
from .models import nodemcu1
from .serializers import Nodemcu1Serializer
# Create your views here.
class Nodemcu1View(viewsets.ModelViewSet):
	queryset=nodemcu1.objects.all()
	serializer_class=Nodemcu1Serializer

class EventDetail(APIView):
    def delete(self, request, pk, format=None):
        event = self.get_object(pk)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
