# Generated by Django 3.1.4 on 2020-12-17 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TeamMembers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fullname', models.CharField(max_length=30)),
                ('designation', models.CharField(max_length=30)),
                ('member_picture', models.ImageField(upload_to='static/images/')),
                ('linkedin_url', models.URLField()),
                ('instagram_url', models.URLField()),
            ],
        ),
    ]
