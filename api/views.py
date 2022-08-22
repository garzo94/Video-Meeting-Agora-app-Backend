from django.shortcuts import render
from rest_framework.response import Response
from api.models import Meeting
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api.serializers import MeetingSerializer
from datetime import datetime, time
from django.utils.timezone import make_aware
# Create your views here.


class CreateMeeting(APIView):
# t("YYYY-MM-DD HH:mm:ss")
    def post(self, request):
        data = request.data
        data['start'] = datetime.strptime(data['start'],'%Y-%m-%d %H:%M:%S')
        print(data['duration'])
        data['duration'] = datetime.strptime(str(data['duration']),'%M').time()
        serializer = MeetingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            print(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self,request, uid):
        meeting =  get_object_or_404(Meeting, uid=uid)
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

