from rest_framework import serializers
from .models import TeamMember
class TeamMembersSerializer(serializers.ModelSerializer):

    class Meta:
        model=TeamMember
        fields=['id','fullname','designation','member_picture','linkedin_url','instagram_url']
