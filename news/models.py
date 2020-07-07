from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=100, null=True, blank=True)
    text = models.TextField()
    image = models.ImageField(upload_to='static/img/', blank=True, null=True)
    date = models.DateTimeField(default=timezone.now, verbose_name=u"Дата")

    def __str__(self):
        return self.title
