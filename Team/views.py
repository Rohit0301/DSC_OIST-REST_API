from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateDestroyAPIView,CreateAPIView
from .models import TeamMember
from .serializers import TeamMembersSerializer
from rest_framework.permissions import IsAdminUser,BasePermission,SAFE_METHODS,IsAuthenticatedOrReadOnly
from rest_framework.authentication import SessionAuthentication
# Create your views here.
class IsAdminUserOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        is_admin = super(
            IsAdminUserOrReadOnly, 
            self).has_permission(request, view)
        # Python3: is_admin = super().has_permission(request, view)
        return request.method in SAFE_METHODS or is_admin

class TeamMemberListView(ListCreateAPIView):
    serializer_class=TeamMembersSerializer
    permission_classes=[IsAdminUserOrReadOnly]
    def get_queryset(self):
        return TeamMember.objects.all()
    def perform_create(self,serializer):
        serializer.save()

# class TeamMemberCreateView(CreateAPIView):
#     serializer_class=TeamMembersSerializer
#     authentication_classes=[SessionAuthentication]
#     permission_classes=[IsAdminUser]
#     def perform_create(self,serializer):
#         serializer.save()


class TeamMemberDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class=TeamMembersSerializer
    authentication_classes=[SessionAuthentication]
    permission_classes=[IsAdminUserOrReadOnly]
    lookup_field="fullname"
        
    def get_queryset(self):
        return TeamMember.objects.filter(fullname__contains=self.kwargs['fullname'])
