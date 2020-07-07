from django.db import models
from accounts.models import CustomUser
from plans.models import Plan
from django.utils import timezone
from django.db.models.signals import post_save
from django.dispatch import receiver


class OrderStatus(models.Model):
    name = models.CharField(max_length=100)
    code = models.IntegerField(max_length=1)

    def __str__(self):
        return self.name


class Order(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.SET_NULL, null=True)
    plan = models.ForeignKey(Plan, on_delete=models.SET_NULL, null=True)
    provider_id = models.IntegerField(max_length=24, blank=True, null=True)
    name = models.CharField(max_length=128, blank=True, null=True)
    amount = models.IntegerField(max_length=24, null=True, blank=True)
    price = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name=u"Цена, руб.")
    total_price = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата")
    comment = models.TextField(blank=True, verbose_name=u"Комментарий")
    charge = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name=u"Возврат, руб.", blank=True,
                                 null=True)
    start_count = models.DecimalField(default=0, max_digits=9, decimal_places=2, blank=True)
    status = models.ForeignKey(OrderStatus, on_delete=models.SET_NULL, blank=True, null=True)
    remains = models.IntegerField(max_length=24, null=True, blank=True)
    video = models.CharField(max_length=256)
    traffic = models.CharField(max_length=128)
    countries = models.CharField(max_length=512)

    def __str__(self):
        return self.name if self.name else str(self.id)

    def save(self, *args, **kwargs):
        if not self.pk:

            if not self.status:
                self.status = OrderStatus.objects.all()[0]

            self.remains = self.amount

        super().save(*args, **kwargs)


@receiver(post_save, sender=Order, dispatch_uid="set_name")
def set_name(sender, instance, **kwargs):
    if not instance.name:
        instance.name = 'Order #{}'.format(instance.id)
        instance.save()