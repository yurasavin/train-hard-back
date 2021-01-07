from rest_framework import serializers

from apps.training_history.models import ExerciseDone, TrainingHistory


class CreateTrainingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingHistory
        fields = ['program']


class TrainingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingHistory
        fields = ['id', 'program', 'start', 'end']


class ExerciseDoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseDone
        fields = [
            'id', 'training_history', 'exercise', 'repeat', 'duration_seconds',
        ]
