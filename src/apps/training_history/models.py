from django.db import models


class TrainingHistory(models.Model):
    start = models.DateTimeField(auto_now_add=True)
    end = models.DateTimeField(null=True)
    program = models.ForeignKey('programs.Program', on_delete=models.PROTECT)


class ExerciseDone(models.Model):
    training_history = models.ForeignKey(
        TrainingHistory, on_delete=models.PROTECT)
    exercise = models.ForeignKey('programs.Exercise', on_delete=models.PROTECT)
    repeat = models.IntegerField()
    duration_seconds = models.PositiveIntegerField()
