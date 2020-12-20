from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Event
from rest_framework.authentication import BasicAuthentication
from .serializers import EventsSerializer
from rest_framework.permissions import IsAdminUser,AllowAny
# Create your views here.

class EventListView(ListAPIView):
    serializer_class=EventsSerializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        return Event.objects.all()

class EventCreateView(CreateAPIView):
    serializer_class=EventsSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAdminUser]
    def perform_create(self,serializer):
        serializer.save()


class EventDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=EventsSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAdminUser]
    lookup_field="title"
        
    def get_queryset(self):
        return Event.objects.filter(title=self.kwargs['title'])
