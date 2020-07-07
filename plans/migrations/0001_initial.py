# Generated by Django 3.0.6 on 2020-05-31 12:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomPlan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=58, verbose_name='Название')),
                ('price', models.DecimalField(decimal_places=2, max_digits=9, verbose_name='Цена')),
                ('provider_id', models.CharField(blank=True, max_length=16, verbose_name='ID сервиса у провайдера')),
            ],
        ),
        migrations.CreateModel(
            name='CustomPlanPrices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('min_amount', models.IntegerField(verbose_name='min N')),
                ('max_amount', models.IntegerField(verbose_name='max N')),
                ('custom_plan', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.CustomPlan')),
            ],
        ),
        migrations.AddField(
            model_name='customplan',
            name='plan',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='plans.Plan'),
        ),
        migrations.AddField(
            model_name='customplan',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
