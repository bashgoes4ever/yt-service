from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class Log(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата")
    event = models.TextField(blank=True, verbose_name=u"Событие")

    def __str__(self):
        return self.date
