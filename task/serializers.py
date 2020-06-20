from rest_framework import serializers,exceptions
from django.contrib.auth import get_user_model
from .models import ActivityPeriods,User


class ActivityPeriodsSerializer(serializers.ModelSerializer):
    start_time = serializers.DateTimeField(format="%B %d %Y %H:%M")
    end_time = serializers.DateTimeField(format="%B %d %Y %H:%M")
    class Meta:
        model = ActivityPeriods
        fields = ['start_time','end_time']

class UserSerializer(serializers.ModelSerializer):
    activity = ActivityPeriodsSerializer(many=True,read_only=True)
    class Meta:
        model = User
        fields = ['id','real_name','tz','activity']


