# Generated by Django 3.1.5 on 2021-02-12 21:03

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('plans', '0002_delete_traininghistory'),
        ('training_history', '0004_auto_20210107_1235'),
        ('programs', '0008_auto_20210105_2012'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Program',
            new_name='Training',
        ),
    ]
