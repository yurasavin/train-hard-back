# Generated by Django 3.1.4 on 2020-12-29 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20201229_2203'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='height',
            field=models.PositiveSmallIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.PositiveSmallIntegerField(null=True),
        ),
    ]
