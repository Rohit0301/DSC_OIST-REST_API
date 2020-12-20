from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import TeamMember
from .serializers import TeamMembersSerializer
from rest_framework.permissions import IsAdminUser,BasePermission,SAFE_METHODS,IsAuthenticated,AllowAny
from rest_framework.authentication import BasicAuthentication
# Create your views here.

class TeamMemberListView(ListAPIView):
    serializer_class=TeamMembersSerializer
    permission_classes=[AllowAny]
    def get_queryset(self):
        return TeamMember.objects.all()

class TeamMemberCreateView(CreateAPIView):
    serializer_class=TeamMembersSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    def perform_create(self,serializer):
        serializer.save()


class TeamMemberDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=TeamMembersSerializer
    authentication_classes=[BasicAuthentication]
    permission_classes=[IsAdminUser]
    lookup_field="fullname"
        
    def get_queryset(self):
        
        return TeamMember.objects.filter(fullname__contains=self.kwargs['fullname'])
