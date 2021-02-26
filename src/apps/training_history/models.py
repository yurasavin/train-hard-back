from django.db import models


class TrainingHistory(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)
    training = models.ForeignKey('programs.Training', on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.start}:{self.end}'


class ExerciseDone(models.Model):
    training_history = models.ForeignKey(
        TrainingHistory, on_delete=models.PROTECT)
    exercise = models.ForeignKey('programs.Exercise', on_delete=models.PROTECT)
    repeat = models.IntegerField()
    duration_seconds = models.PositiveIntegerField()

    def __str__(self):
        return f'{self.id}-{self.repeat}'
