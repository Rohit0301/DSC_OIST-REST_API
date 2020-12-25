from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Event
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
from .serializers import EventsSerializer
from rest_framework.permissions import IsAdminUser,AllowAny,SAFE_METHODS
# Create your views here.
class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class EventListView(ListCreateAPIView):
    serializer_class=EventsSerializer
    permission_classes=[IsAdminUserOrReadOnly]
    def get_queryset(self):
        return Event.objects.all()
    def perform_create(self,serializer):
        serializer.save()

# class EventCreateView(CreateAPIView):
#     serializer_class=EventsSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAdminUser]
#     def perform_create(self,serializer):
#         serializer.save()


class EventDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=EventsSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUserOrReadOnly]
    lookup_field="title"
        
    def get_queryset(self):
        return Event.objects.filter(title=self.kwargs['title'])
