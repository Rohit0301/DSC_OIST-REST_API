from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Resource
from .serializers import ResourcesSerializer
from rest_framework import permissions
# Create your views here.

class ResourseListView(ListAPIView):
    serializer_class=ResourcesSerializer

    def get_queryset(self):
        return Resource.objects.all()

class ResourceCreateView(CreateAPIView):
    serializer_class=ResourcesSerializer
    permission_classes=(permissions.IsAdminUser,)
    def perform_create(self,serializer):
        serializer.save()


class ResourceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=ResourcesSerializer
    # permission_classes=(permissions.IsAuthenticated,)
    lookup_field="id"
        
    def get_queryset(self):
        return Resource.objects.filter(id=self.kwargs['id'])
