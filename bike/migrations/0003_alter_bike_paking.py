# Generated by Django 3.2.7 on 2021-11-23 14:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bike', '0002_bike_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bike',
            name='paking',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='paking', to='bike.paking'),
        ),
    ]
