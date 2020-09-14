# Generated by Django 3.1.1 on 2020-09-13 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shorten',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('long_url', models.CharField(max_length=2500)),
                ('times_viewed', models.BigIntegerField(default=0)),
            ],
        ),
    ]