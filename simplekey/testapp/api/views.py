from rest_framework import viewsets
from testapp.models import Buy,Rent,Land,Agent
from testapp.api.serializers import BuySerializer,RentSerializer,LandSerializer,AgentSerializer
class BuyAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class=BuySerializer
    queryset=Buy.objects.all()

class RentAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class=RentSerializer
    queryset=Rent.objects.all()

class LandAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class=LandSerializer
    queryset=Land.objects.all()

class AgentAPI(viewsets.ReadOnlyModelViewSet):
    serializer_class=AgentSerializer
    queryset=Agent.objects.all()


