# Generated by Django 3.2.7 on 2021-11-19 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bike',
            name='image',
            field=models.TextField(null=True),
        ),
    ]
