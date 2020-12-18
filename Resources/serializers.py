from rest_framework import serializers
from .models import Resource
class ResourcesSerializer(serializers.ModelSerializer):

    class Meta:
        model=Resource
        fields=['id','name','domain','resource_url','resource_file']
