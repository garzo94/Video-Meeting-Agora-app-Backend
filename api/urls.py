from django.urls import path
from api.views import CreateMeeting, UserMeeting


urlpatterns=[
    path('api/my_room/', CreateMeeting.as_view(), name='room'),
    path('api/my_room/<str:uidMeeting>/', CreateMeeting.as_view(), name='room'),
    path('api/room_meeting/<str:uidMeeting>/', UserMeeting.as_view(), name='room-meeting'),

    ]
