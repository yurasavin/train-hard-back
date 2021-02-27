from django.conf import settings
from django.db import models


class Program(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name


class Training(models.Model):
    name = models.CharField(max_length=150)
    rest_between_exercises = models.DurationField()
    rest_between_repeats = models.DurationField()
    program = models.ForeignKey(
        Program, on_delete=models.CASCADE, null=True, related_name='trainings')

    def __str__(self) -> str:
        return self.name


class Inventory(models.IntegerChoices):
    NONE = (0, 'Ничего')
    BARBELL = (1, 'Штанга')
    DUMBBELL = (2, 'Гантели')
    KETTLEBELL = (3, 'Гиря')


class Exercise(models.Model):
    order = models.PositiveSmallIntegerField('Порядковый номер', default=1)
    name = models.CharField('Название', max_length=150)
    inventory = models.IntegerField(
        'Инвентарь', choices=Inventory.choices, default=Inventory.NONE)
    weight = models.DecimalField('Вес', max_digits=5, decimal_places=2)
    approaches = models.PositiveSmallIntegerField('Подходов', default=1)
    repeats = models.PositiveSmallIntegerField('Повторений', default=1)
    updated_at = models.DateTimeField('Обновлено', auto_now=True)
    training = models.ForeignKey(
        Training, verbose_name='Тренировка', on_delete=models.SET_NULL,
        null=True, related_name='exercises')

    class Meta:
        ordering = ['training_id', 'order']

    def __str__(self) -> str:
        return (
            f'{self.name}: {self.approaches}x{self.repeats} ({self.weight} кг)'
        )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._approaches = self.approaches
        self._repeats = self.repeats
        self._weight = self.weight

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)

        if (self._weight and self._weight != self.weight or
                self._repeats and self._repeats != self.repeats or
                self._approaches and self._approaches != self.approaches):
            self.exercisehistory_set.create(
                weight=self.weight,
                repeats=self.repeats,
                approaches=self.approaches)

        return ret


class ExerciseHistory(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    repeats = models.PositiveSmallIntegerField()
    approaches = models.PositiveSmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return str(self.exercise)
