from rest_framework import serializers

from apps.programs.models import Exercise, Program, Training


class ExerciseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Exercise
        fields = [
            'id', 'order', 'name', 'inventory', 'weight', 'approaches',
            'repeats',
        ]


class TrainingListSerializer(serializers.ModelSerializer):
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Training
        fields = ['id', 'name', 'exercises']


class TrainingDetailSerializer(serializers.ModelSerializer):
    rest_between_exercises = serializers.SerializerMethodField()
    rest_between_repeats = serializers.SerializerMethodField()
    exercises = ExerciseSerializer(many=True)

    class Meta:
        model = Training
        fields = [
            'id', 'name', 'rest_between_exercises', 'rest_between_repeats',
            'exercises',
        ]

    def get_rest_between_exercises(self, obj):
        return int(obj.rest_between_exercises.total_seconds())

    def get_rest_between_repeats(self, obj):
        return int(obj.rest_between_repeats.total_seconds())


class ProgramSerializer(serializers.ModelSerializer):
    trainings = TrainingListSerializer(many=True)

    class Meta:
        model = Program
        fields = ['id', 'name', 'trainings']
