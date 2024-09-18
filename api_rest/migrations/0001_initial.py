# Generated by Django 5.1.1 on 2024-09-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_nickname', models.CharField(default='', max_length=50, primary_key=True, serialize=False)),
                ('user_name', models.CharField(default='', max_length=150)),
                ('user_email', models.EmailField(default='', max_length=150)),
                ('user_age', models.IntegerField(default=0)),
            ],
        ),
    ]
