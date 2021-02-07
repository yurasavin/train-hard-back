from django.contrib import admin

from apps.training_history.models import ExerciseDone, TrainingHistory


class TrainingHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'program',
        'start',
        'end',
    ]


class ExerciseDoneAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'training_history',
        'exercise',
        'repeat',
        'duration_seconds',
    ]


admin.site.register(TrainingHistory, TrainingHistoryAdmin)
admin.site.register(ExerciseDone, ExerciseDoneAdmin)
