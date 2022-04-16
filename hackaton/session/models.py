from django.db import models
from django.conf import settings


class Session(models.Model):
    name = models.CharField(max_length=1000)
    hours_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    percent = models.FloatField()
    law_number = models.CharField(max_length=50)
    status = models.CharField(max_length=70)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_number = models.IntegerField()


class SessionData(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    betting_time = models.DateTimeField(auto_now_add=True)
    current_amount = models.FloatField()
    session_id = models.ForeignKey(Session, on_delete=models.PROTECT)