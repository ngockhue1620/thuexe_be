# Generated by Django 3.2.7 on 2021-11-19 01:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_bike_image'),
        ('card', '0002_auto_20211119_0755'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bike', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bike_order', to='bike.bike')),
                ('card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='card_order', to='card.card')),
            ],
        ),
    ]
