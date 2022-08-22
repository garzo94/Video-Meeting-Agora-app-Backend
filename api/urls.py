from django.urls import path
from api.views import CreateMeeting


urlpatterns=[
    path('api/my_room/', CreateMeeting.as_view(), name='room'),
    path('api/my_room/<str:uid>/', CreateMeeting.as_view(), name='room'),

    ]
