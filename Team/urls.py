from django.contrib import admin
from django.urls import path,include
from .views import TeamMemberListView,TeamMemberDetailView
urlpatterns = [
  path('TeamMembers/',TeamMemberListView.as_view()),
  # path('AddMember/',TeamMemberCreateView.as_view()),
  path('TeamMembers/<fullname>/',TeamMemberDetailView.as_view()),
]
