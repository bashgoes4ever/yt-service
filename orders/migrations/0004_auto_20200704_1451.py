# Generated by Django 3.0.6 on 2020-07-04 04:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_auto_20200704_1214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='name',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
