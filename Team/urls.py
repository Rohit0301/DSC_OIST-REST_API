from django.contrib import admin
from django.urls import path,include
from .views import TeamMemberListView,TeamMemberCreateView,TeamMemberDetailView
urlpatterns = [
  path('teammembers/',TeamMemberListView.as_view()),
  path('addmember/',TeamMemberCreateView.as_view()),
  path('memberdetails/<id>/',TeamMemberDetailView.as_view()),
]
