# Generated by Django 5.1.7 on 2025-03-30 08:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_user_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='password',
            field=models.CharField(default='', max_length=128),
        ),
        migrations.AddField(
            model_name='user',
            name='role',
            field=models.CharField(default='Intern', max_length=100),
        ),
    ]
