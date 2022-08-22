from django.db import models

# Create your models here.
class Meeting(models.Model):
    uid = models.CharField(max_length=50)
    start = models.DateTimeField()
    duration = models.TimeField()
    room_name = models.CharField(max_length=100)
