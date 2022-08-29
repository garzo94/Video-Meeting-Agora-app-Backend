from django.db import models

# Create your models here.
class Meeting(models.Model):
    uid = models.CharField(max_length=50)
    start = models.DateTimeField()
    duration = models.TimeField()
    room_name = models.CharField(max_length=100)

    def __str__(self):
        return self.room_name

class User(models.Model):
    name = models.CharField(max_length=50,)
    uid = models.CharField(max_length=100, blank=True, null=True)
    token = models.CharField(max_length=500,blank=True, null=True)
    room_name = models.ForeignKey(Meeting, on_delete=models.CASCADE,blank=True, null=True)

    def __str__(self):
        return self.name
