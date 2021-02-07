from django.conf import settings
from django.db import models


class PostgresWeekdays(models.IntegerChoices):
    MONDAY = (2, 'Понедельник')
    TUESDAY = (3, 'Вторник')
    WEDNESDAY = (4, 'Среда')
    THURSDAY = (5, 'Четверг')
    FRIDAY = (6, 'Пятница')
    SATURDAY = (7, 'Суббота')
    SUNDAY = (1, 'Воскресенье')


class PythonWeekdays(models.IntegerChoices):
    MONDAY = (0, 'Понедельник')
    TUESDAY = (1, 'Вторник')
    WEDNESDAY = (2, 'Среда')
    THURSDAY = (3, 'Четверг')
    FRIDAY = (4, 'Пятница')
    SATURDAY = (5, 'Суббота')
    SUNDAY = (6, 'Воскресенье')


PYTHON_WEEKDAY_TO_POSTGRES_WEEKDAY = {
    0: 2,
    1: 3,
    2: 4,
    3: 5,
    4: 6,
    5: 7,
    6: 1,
}


class TrainigPlan(models.Model):
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.id


class Schedule(models.Model):
    weekday = models.PositiveIntegerField(choices=PythonWeekdays.choices)
    program = models.ForeignKey('programs.Program', on_delete=models.PROTECT)
    training_plan = models.ForeignKey(TrainigPlan, on_delete=models.CASCADE)

    def __str__(self):
        return self.id
