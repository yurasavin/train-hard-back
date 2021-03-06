from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet

from apps.api.serializers.training_history import (
    CreateTrainingHistorySerializer, ExerciseDoneSerializer,
    TrainingHistorySerializer)
from apps.training_history.models import ExerciseDone, TrainingHistory


class TrainingHistoryViewSet(GenericViewSet):
    queryset = TrainingHistory.objects.all()
    serializer_class = TrainingHistorySerializer

    @action(detail=False, methods=['post'])
    def check(self, request):
        serializer = CreateTrainingHistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        started_training = TrainingHistory.objects \
            .filter(training_id=serializer.validated_data['training'].id,
                    start__date=timezone.now().date()) \
            .exists()
        response_data = {'started_training': started_training}
        return Response(response_data)

    @action(detail=False, methods=['post'])
    def start(self, request):
        serializer = CreateTrainingHistorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response_serializer = TrainingHistorySerializer(
            instance=serializer.instance)
        return Response(
            response_serializer.data, status=status.HTTP_201_CREATED)

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
