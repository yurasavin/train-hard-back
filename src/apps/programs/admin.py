from django.contrib import admin

from apps.programs.models import Exercise, ExerciseHistory, Program


class ExerciseAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'program',
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


class ProgramAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'name',
        'owner',
        'rest_between_exercises',
        'rest_between_repeats',
    ]


admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(ExerciseHistory, ExerciseHistoryAdmin)
admin.site.register(Program, ProgramAdmin)
