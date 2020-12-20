from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Resource
from .serializers import ResourcesSerializer
from rest_framework.permissions import IsAdminUser,AllowAny
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class ResourceListView(ListAPIView):
    serializer_class=ResourcesSerializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        return Resource.objects.all()

class ResourceCreateView(CreateAPIView):
    serializer_class=ResourcesSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAdminUser]
    def perform_create(self,serializer):
        serializer.save()


class ResourceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=ResourcesSerializer
    # authentication_classes=[BasicAuthentication]
    # permission_classes=[IsAdminUser]
    lookup_field="name"
        
    def get_queryset(self):
        return Resource.objects.filter(name=self.kwargs['name'])
