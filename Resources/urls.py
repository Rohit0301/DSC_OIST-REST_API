from django.contrib import admin
from django.urls import path,include
from .views import ResourceListView,ResourceDetailView
urlpatterns = [
  path('Resource/',ResourceListView.as_view()),
  # path('AddNewResource/',ResourceCreateView.as_view()),
  path('Resource/<name>/',ResourceDetailView.as_view()),
]
