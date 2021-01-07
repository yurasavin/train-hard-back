from rest_framework import serializers

from apps.programs.models import Exercise, Program


class ProgramSerializer(serializers.ModelSerializer):
    rest_between_exercises = serializers.SerializerMethodField()
    rest_between_repeats = serializers.SerializerMethodField()

    class Meta:
        model = Program
        fields = [
            'id', 'name', 'rest_between_exercises', 'rest_between_repeats',
        ]

    def get_rest_between_exercises(self, obj):
        return int(obj.rest_between_exercises.total_seconds())

    def get_rest_between_repeats(self, obj):
        return int(obj.rest_between_repeats.total_seconds())


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = ['id', 'name', 'inventory', 'weight', 'approaches', 'repeats']
