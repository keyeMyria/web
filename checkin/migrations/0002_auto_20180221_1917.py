# Generated by Django 2.0.2 on 2018-02-21 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('checkin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userskill',
            name='skill_level',
            field=models.IntegerField(choices=[(1, 'Nybegynner'), (2, 'Viderekommen'), (3, 'Ekspert')]),
        ),
    ]