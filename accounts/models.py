from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from datetime import datetime
from datetime import timedelta
from django.conf import settings
import jwt

from .managers import CustomUserManager


class CustomUserSite(models.Model):
    name = models.CharField(max_length=24, blank=False, verbose_name=u"Название")

    def __str__(self):
        return self.name


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_('email address'), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now, verbose_name=u"Дата регистрации")
    comment = models.TextField(blank=True, verbose_name=u"Комментарий", null=True)
    amount = models.DecimalField(default=0, max_digits=9, decimal_places=2, verbose_name=u"Сумма", db_column="amount")
    site = models.ForeignKey(CustomUserSite, related_name='site', null=True, on_delete=models.CASCADE, blank=True, verbose_name=u"Сайт")
    api_token = models.CharField(max_length=58, blank=True)
    a_field = models.CharField(max_length=24, blank=True, verbose_name=u"A")
    last_visit = models.DateTimeField(blank=True, null=True, verbose_name=u"Последний визит")

    # @property
    # def amount(self):
    #     return self._amount
    #
    # @amount.setter
    # def amount(self, value):
    #     self._amount = self._amount + value

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def add_amount(self, amount, type=None):
        self.amount = self.amount + int(amount)

    def __str__(self):
        return self.email

    @property
    def token(self):
        return self._generate_jwt_token()

    def _generate_jwt_token(self):
        token = jwt.encode({
            'id': self.pk,
            'exp': datetime.now() + timedelta(days=60)
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')