from django.db import models
from accounts.models import CustomUser


class Plan(models.Model):
    name = models.CharField(max_length=58, verbose_name=u"Название")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u"Цена")
    provider_id = models.CharField(max_length=16, null=True, blank=True, verbose_name=u"ID сервиса у провайдера")

    def __str__(self):
        return self.name


class CustomPlanPrices(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    plan = models.ForeignKey(Plan, on_delete=models.CASCADE)
    min_amount = models.IntegerField(verbose_name=u"min N")
    max_amount = models.IntegerField(verbose_name=u"max N")
    price = models.DecimalField(max_digits=9, decimal_places=2, verbose_name=u"Цена")

    def __str__(self):
        return self.plan.name

