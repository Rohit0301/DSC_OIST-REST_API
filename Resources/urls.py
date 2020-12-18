from django.contrib import admin
from django.urls import path,include
from .views import ResourceListView,ResourceCreateView,ResourceDetailView
urlpatterns = [
  path('AllResources/',ResourceListView.as_view()),
  path('AddNewResource/',ResourceCreateView.as_view()),
  path('Resource/<id>/',ResourceDetailView.as_view()),
]
