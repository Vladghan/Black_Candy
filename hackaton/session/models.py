from django.db import models
from django.conf import settings

from account.forms import CustomUser


class Session(models.Model):
    TYPE_OF_STATUS = [
        ('active', 'активна'),
        ('complete', 'проведена'),
        ('fall', 'не состоялась'),
        ('deleted', 'снята с публикации'),
    ]
    TYPE_OF_LOW = [
        (44, '44 ФЗ'),
        (223, '223 ФЗ'),
    ]
    name = models.CharField(max_length=1000)
    hours_number = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    percent = models.FloatField()
    law_number = models.IntegerField(choices=TYPE_OF_LOW)
    status = models.CharField(max_length=10, choices=TYPE_OF_STATUS)
    client = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session_number = models.IntegerField()
    start_price = models.FloatField()

    def __str__(self):
        return self.name


class UserSession(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.Model)
    session = models.ForeignKey(Session, on_delete=models.Model, related_name='user_sessions')
    limit_price = models.FloatField(blank=True, null=True)
    limit_time = models.DateTimeField(blank=True, null=True)
    robot = models.BooleanField(default=False)


class SessionData(models.Model):
    provider = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    betting_time = models.DateTimeField(auto_now_add=True)
    current_amount = models.FloatField()
    session_id = models.ForeignKey(Session, on_delete=models.PROTECT, related_name='sessions_data')

    class Meta:
        ordering = ['current_amount']
