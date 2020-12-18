from django.contrib import admin
from django.urls import path,include
from .views import TeamMemberListView,TeamMemberCreateView,TeamMemberDetailView
urlpatterns = [
  path('TeamMembers/',TeamMemberListView.as_view()),
  path('AddMember/',TeamMemberCreateView.as_view()),
  path('MemberDetails/<fullname>/',TeamMemberDetailView.as_view()),
]
