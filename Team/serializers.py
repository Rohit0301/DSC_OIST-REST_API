from rest_framework import serializers
from .models import TeamMembers
class TeamMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model=TeamMembers
        fields=['fullname','designation','member_picture','linkedin_url','instagram_url']
        