# Generated by Django 3.1.4 on 2020-12-18 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('subtitle', models.CharField(max_length=80, null=True)),
                ('description', models.CharField(max_length=200, null=True)),
                ('speaker', models.CharField(max_length=30)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('event_url', models.URLField(null=True)),
            ],
        ),
    ]
