# Generated by Django 3.1.4 on 2021-01-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('training_history', '0002_auto_20210105_2043'),
    ]

    operations = [
        migrations.AddField(
            model_name='exercisedone',
            name='duration_seconds',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
