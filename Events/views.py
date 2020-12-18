from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Event
from .serializers import EventsSerializer
from rest_framework import permissions
# Create your views here.

class EventListView(ListAPIView):
    serializer_class=EventsSerializer

    def get_queryset(self):
        return Event.objects.all()

class EventCreateView(CreateAPIView):
    serializer_class=EventsSerializer
    permission_classes=(permissions.IsAdminUser,)
    def perform_create(self,serializer):
        serializer.save()


class EventDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=EventsSerializer
    # permission_classes=(permissions.IsAuthenticated,)
    lookup_field="id"
        
    def get_queryset(self):
        return Event.objects.filter(id=self.kwargs['id'])
