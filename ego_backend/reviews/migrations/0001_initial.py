# Generated by Django 3.2.2 on 2023-12-18 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.FloatField(default=0.0, max_length=3)),
                ('username', models.CharField(max_length=30)),
                ('content', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
