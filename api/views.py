from django.shortcuts import render
from rest_framework.response import Response
from api.models import Meeting, User
from rest_framework import status
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404
from api.serializers import MeetingSerializer, UserSerializer
from datetime import datetime, time
import random
from agora_token_builder import RtcTokenBuilder
import time
# Create your views here.


class CreateMeeting(APIView):

    def post(self, request):
        data = request.data
        data['start'] = datetime.strptime(data['start'],'%Y-%m-%d %H:%M')
        data['duration'] = datetime.strptime(str(data['duration']),'%M').time()
        serializer = MeetingSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            print(serializer.errors)
            print(serializer.data)
            return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)

    def get(self,request, uidMeeting):
        meeting =  get_object_or_404(Meeting, uid=uidMeeting)
        serializer = MeetingSerializer(meeting)
        return Response(serializer.data)

class UserMeeting(APIView):
    def post(self, request, uidMeeting):
        name = request.data
        channelName = get_object_or_404(Meeting, uid=uidMeeting)
        appId = "77780af0adae470b9bf4d235b64c14c4"
        appCertificate = "b5cae2a165904c2f90c24f30803696fb"
        uid = random.randint(1, 230)
        expirationTimeInSeconds = 3600
        currentTimeStamp = int(time.time())
        privilegeExpiredTs = currentTimeStamp + expirationTimeInSeconds
        role = 1
        token = RtcTokenBuilder.buildTokenWithUid(appId, appCertificate, channelName.room_name, uid, role, privilegeExpiredTs)
        User.objects.create(name=name,uid=uid,token=token,room_name=channelName)

        return Response({'name':name['name'], 'uid':uid, 'token':token, 'channel':channelName.room_name})




