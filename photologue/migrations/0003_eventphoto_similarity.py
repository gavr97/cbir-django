# Generated by Django 2.1.8 on 2019-04-28 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photologue', '0002_photosize_data'),
    ]

    operations = [
        migrations.AddField(
            model_name='eventphoto',
            name='similarity',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
