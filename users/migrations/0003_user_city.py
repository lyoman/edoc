# Generated by Django 3.1.7 on 2021-03-20 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20210319_2336'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='city',
            field=models.TextField(default='Harare'),
        ),
    ]
