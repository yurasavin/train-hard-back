from rest_framework import serializers

from apps.training_history.models import ExerciseDone, TrainingHistory


class CreateTrainingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingHistory
        fields = ['training']


class TrainingHistorySerializer(serializers.ModelSerializer):

    class Meta:
        model = TrainingHistory
        fields = ['id', 'training', 'start', 'end']


class ExerciseDoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = ExerciseDone
        fields = [
            'id', 'training_history', 'exercise', 'repeat', 'duration_seconds',
        ]
