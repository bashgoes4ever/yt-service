# Generated by Django 3.0.6 on 2020-06-26 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20200531_1855'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='comment',
            field=models.TextField(blank=True, null=True, verbose_name='Комментарий'),
        ),
    ]
