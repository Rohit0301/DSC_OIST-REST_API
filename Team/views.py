from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import TeamMembers 
from .serializers import TeamMembersSerializer
from rest_framework import permissions
# Create your views here.

class ContactListView(ListAPIView):
    serializer_class=TeamMembersSerializer

    def get_queryset(self):
        return TeamMembers.objects.get()

# class ContactDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class=TeamMembersSerializer
#     permission_classes=(permissions.IsAuthenticated,)
#     lookup_field="id"
        
#     def get_queryset(self):
#         return Contact.objects.filter(owner=self.request.user)
