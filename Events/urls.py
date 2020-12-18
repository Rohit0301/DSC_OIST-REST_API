from django.contrib import admin
from django.urls import path,include
from .views import EventListView,EventCreateView,EventDetailView
urlpatterns = [
  path('AllEvents/',EventListView.as_view()),
  path('AddNewEvent/',EventCreateView.as_view()),
  path('Event/<id>/',EventDetailView.as_view()),
]
