# Generated by Django 2.1.5 on 2019-01-18 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('slug', models.SlugField(max_length=20)),
                ('time', models.TimeField()),
                ('date', models.DateField()),
                ('prize', models.IntegerField()),
                ('kills', models.IntegerField()),
                ('fees', models.IntegerField()),
                ('type', models.CharField(choices=[(1, 'Solo'), (2, 'Duo'), (3, 'Squad')], default='1', max_length=6)),
                ('version', models.CharField(choices=[(1, 'TPP'), (2, 'FPP')], default=1, max_length=4)),
                ('map', models.CharField(choices=[(1, 'Erangel'), (2, 'Miramar'), (3, 'Sanhok'), (4, 'Vikendi')], default='1', max_length=8)),
            ],
        ),
    ]
