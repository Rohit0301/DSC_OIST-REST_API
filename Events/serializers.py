from rest_framework import serializers
from .models import Event
class EventsSerializer(serializers.ModelSerializer):

    class Meta:
        model=Event
        fields=['id','title','subtitle','description','speaker','date','time','event_url']
