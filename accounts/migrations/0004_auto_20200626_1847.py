# Generated by Django 3.0.6 on 2020-06-26 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20200626_1809'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='site',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='site', to='accounts.CustomUserSite', verbose_name='Сайт'),
        ),
    ]