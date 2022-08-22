from rest_framework import serializers
from api.models import Meeting


class MeetingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Meeting
        exclude = ['id']