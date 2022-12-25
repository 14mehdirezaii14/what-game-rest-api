from whatGame.models import Ticket
from whatGame.models import EscapeRoom
from whatGame.models import disableDate
from rest_framework import serializers


class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ticket
        fields = '__all__'
        
class EscapeRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = EscapeRoom
        fields = '__all__'
        
        
class disableDateSerializer(serializers.ModelSerializer):
    class Meta:
        model = disableDate
        fields = '__all__'