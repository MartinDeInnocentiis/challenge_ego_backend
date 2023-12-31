# Generated by Django 3.2.2 on 2023-12-18 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('datetime', models.DateTimeField(blank=True, null=True)),
                ('address', models.CharField(blank=True, max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Financing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jsonfield', models.JSONField()),
            ],
        ),
    ]
