from rest_framework.serializers import ModelSerializer
from testapp.models import Buy,Rent,Land,Agent
class BuySerializer(ModelSerializer):

    class Meta:

        model=Buy

        fields='__all__'

class RentSerializer(ModelSerializer):

    class Meta:

        model=Rent

        fields='__all__'

class LandSerializer(ModelSerializer):

    class Meta:

        model=Land

        fields='__all__'

class AgentSerializer(ModelSerializer):

    class Meta:

        model=Agent

        fields='__all__'
