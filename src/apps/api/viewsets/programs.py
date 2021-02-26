from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin,
                                   UpdateModelMixin)
from rest_framework.viewsets import GenericViewSet

from apps.api.serializers.programs import (ExerciseSerializer,
                                           ProgramSerializer,
                                           TrainingDetailSerializer)
from apps.programs.models import Exercise, Program, Training


class ProgramListView(ListModelMixin, GenericViewSet):
    queryset = Program.objects.all().prefetch_related('trainings__exercises')
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return self.queryset.filter(owner_id=self.request.user.id)


class TrainingDetailView(RetrieveModelMixin, GenericViewSet):
    queryset = Training.objects.all()
    serializer_class = TrainingDetailSerializer

    def get_queryset(self):
        return self.queryset.filter(program__owner_id=self.request.user.id)


class ExerciseUpdateView(UpdateModelMixin, GenericViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        return self.queryset.filter(
            training__program__owner_id=self.request.user.id)
