# Generated by Django 3.1.4 on 2021-01-07 09:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('training_history', '0003_exercisedone_duration_seconds'),
    ]

    operations = [
        migrations.RenameField(
            model_name='exercisedone',
            old_name='repeats',
            new_name='repeat',
        ),
    ]
