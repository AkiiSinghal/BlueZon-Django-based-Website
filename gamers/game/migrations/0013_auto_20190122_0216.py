# Generated by Django 2.1.3 on 2019-01-21 20:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0012_auto_20190121_1347'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='email',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='fname',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='lname',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userprofileinfo',
            name='username',
        ),
    ]
