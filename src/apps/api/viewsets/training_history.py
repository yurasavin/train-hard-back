from django.utils import timezone

from rest_framework import status
from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.api.serializers.training_history import (
    ExerciseDoneSerializer,
    CreateTrainingHistorySerializer,
    TrainingHistorySerializer)
from apps.training_history.models import ExerciseDone, TrainingHistory


class TrainingHistoryViewSet(GenericViewSet):
    queryset = TrainingHistory.objects.all()
    serializer_class = TrainingHistorySerializer

    @action(detail=False, methods=['post'])
    def start(self, request):
        serializer = CreateTrainingHistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        resonse_serializer = TrainingHistorySerializer(
            instance=serializer.instance)
        return Response(
            resonse_serializer.data, status=status.HTTP_201_CREATED)

    @action(detail=True, methods=['post'])
    def end(self, request, pk=None):
        training = self.get_object()
        training.end = timezone.now()
        training.save()
        serializer = TrainingHistorySerializer(instance=training)
        return Response(serializer.data)


class ExerciseDoneViewSet(CreateModelMixin, GenericViewSet):
    queryset = ExerciseDone.objects.all()
    serializer_class = ExerciseDoneSerializer
