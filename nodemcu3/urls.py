from django.urls import path,include
from . import views
from rest_framework import routers

router=routers.DefaultRouter()
router.register('nodemcu3',views.Nodemcu3View)

urlpatterns = [
    path('',include(router.urls)),
    path(r'^delete/(?P<pk>\d+)',views.EventDetail.as_view(), name='delete_event'),
    
]