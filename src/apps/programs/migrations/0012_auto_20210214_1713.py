# Generated by Django 3.1.5 on 2021-02-14 14:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('programs', '0011_auto_20210213_0017'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='training',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='exercises', to='programs.training', verbose_name='Тренировка'),
        ),
        migrations.AlterField(
            model_name='training',
            name='program',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='trainings', to='programs.program'),
        ),
    ]
