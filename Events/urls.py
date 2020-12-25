from django.contrib import admin
from django.urls import path,include
from .views import EventListView,EventDetailView
urlpatterns = [
  path('Event/',EventListView.as_view()),
  # path('AddNewEvent/',EventCreateView.as_view()),
  path('Event/<title>/',EventDetailView.as_view()),
]
