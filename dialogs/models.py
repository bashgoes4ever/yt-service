from django.db import models
from accounts.models import CustomUser
from django.utils import timezone


class ProblemType(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title


class Dialog(models.Model):
    customer = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=100, null=True, blank=True)
    order_id = models.IntegerField(max_length=24, null=True, blank=True)
    problem_type = models.ForeignKey(ProblemType, on_delete=models.SET_NULL, null=True)
    status = models.IntegerField(max_length=1, default=0)
    date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата")

    def __str__(self):
        return self.title


class Message(models.Model):
    dialog = models.ForeignKey(Dialog, on_delete=models.SET_NULL, null=True)
    message = models.TextField()
    sender = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата")

    def __str__(self):
        return self.date
