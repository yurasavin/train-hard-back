from django.contrib import admin

from apps.programs.models import Exercise, ExerciseHistory, Program, Training


class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'training',
        'order',
        'name',
        'inventory',
        'weight',
        'approaches',
        'repeats',
        'updated_at',
    ]


class ExerciseHistoryAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'exercise',
        'weight',
        'repeats',
        'created_at',
    ]


class TrainingAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'program',
        'rest_between_exercises',
        'rest_between_repeats',
    ]


class ProgramAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'owner',
    ]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseHistory, ExerciseHistoryAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(Program, ProgramAdmin)
