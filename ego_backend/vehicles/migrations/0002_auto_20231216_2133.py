# Generated by Django 3.2.2 on 2023-12-17 00:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='delaerships',
            field=models.ManyToManyField(to='vehicles.Dealership'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='category',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='vehicles.category'),
        ),
    ]
