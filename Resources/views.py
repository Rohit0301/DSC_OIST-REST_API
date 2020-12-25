from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import Resource
from .serializers import ResourcesSerializer
from rest_framework.permissions import IsAdminUser,AllowAny,SAFE_METHODS
from rest_framework.authentication import BasicAuthentication,SessionAuthentication
# Create your views here.
class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class ResourceListView(ListCreateAPIView):
    serializer_class=ResourcesSerializer
    permission_classes=[IsAdminUserOrReadOnly]
    def get_queryset(self):
        return Resource.objects.all()
    def perform_create(self,serializer):
        serializer.save()

# class ResourceCreateView(CreateAPIView):
#     serializer_class=ResourcesSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAdminUser]
#     def perform_create(self,serializer):
#         serializer.save()


class ResourceDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=ResourcesSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUserOrReadOnly]
    lookup_field="name"
        
    def get_queryset(self):
        return Resource.objects.filter(name=self.kwargs['name'])
