# Generated by Django 3.2.2 on 2023-12-17 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0008_auto_20231217_1944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accessory',
            name='dealerships',
            field=models.ManyToManyField(to='vehicles.Dealership'),
        ),
        migrations.AlterField(
            model_name='service',
            name='dealerships',
            field=models.ManyToManyField(to='vehicles.Dealership'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='dealerships',
            field=models.ManyToManyField(to='vehicles.Dealership'),
        ),
    ]
