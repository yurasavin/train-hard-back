# Generated by Django 3.1.4 on 2020-12-29 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_weighthistory_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AlterField(
            model_name='weighthistory',
            name='weight',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
