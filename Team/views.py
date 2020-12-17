from django.shortcuts import render
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import TeamMember
from .serializers import TeamMembersSerializer
from rest_framework import permissions
# Create your views here.

class TeamMemberListView(ListAPIView):
    serializer_class=TeamMembersSerializer

    def get_queryset(self):
        return TeamMember.objects.all()

class TeamMemberCreateView(CreateAPIView):
    serializer_class=TeamMembersSerializer
    permission_classes=(permissions.IsAdminUser,)
    def perform_create(self,serializer):
        serializer.save()


# class ContactDetailView(RetrieveUpdateDestroyAPIView):
#     serializer_class=TeamMembersSerializer
#     permission_classes=(permissions.IsAuthenticated,)
#     lookup_field="id"
        
#     def get_queryset(self):
#         return Contact.objects.filter(owner=self.request.user)
