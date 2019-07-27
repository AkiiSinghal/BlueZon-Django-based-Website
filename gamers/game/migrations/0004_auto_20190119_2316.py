# Generated by Django 2.1.5 on 2019-01-19 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0003_login_profile_register'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.AddField(
            model_name='login',
            name='username',
            field=models.CharField(db_index=True, default=12, max_length=25, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='profile',
            name='username',
            field=models.CharField(db_index=True, default='AkiiSinghal', max_length=25, unique=True),
        ),
        migrations.AlterField(
            model_name='register',
            name='email',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='register',
            name='username',
            field=models.CharField(db_index=True, max_length=25, unique=True),
        ),
    ]
