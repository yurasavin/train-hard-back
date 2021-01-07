from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    birthday = models.DateField(null=True)
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    height = models.PositiveSmallIntegerField(null=True)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._weight = self.weight

    def save(self, *args, **kwargs):
        ret = super().save(*args, **kwargs)
        if self._weight and self._weight != self.weight:
            self.weighthistory_set.create(weight=self.weight)
        return ret


class WeightHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    weight = models.DecimalField(max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
