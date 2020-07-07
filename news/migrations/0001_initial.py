# Generated by Django 3.0.6 on 2020-06-25 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('text', models.TextField()),
                ('image', models.ImageField(upload_to='static/img/')),
            ],
        ),
    ]
