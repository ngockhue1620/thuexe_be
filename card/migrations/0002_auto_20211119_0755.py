# Generated by Django 3.2.7 on 2021-11-19 00:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='blance',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='type',
            field=models.CharField(max_length=2, null=True),
        ),
    ]
