# Generated by Django 3.2.7 on 2021-12-02 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0004_auto_20211123_2041'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, null=True),
        ),
    ]
