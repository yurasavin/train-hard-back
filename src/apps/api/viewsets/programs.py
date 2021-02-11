from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.api.serializers.programs import ExerciseSerializer, ProgramSerializer
from apps.programs.models import Exercise, Program


class ProgramViewSet(ListModelMixin, GenericViewSet):
    queryset = Program.objects.all()
    serializer_class = ProgramSerializer

    def get_queryset(self):
        return self.queryset.filter(owner_id=self.request.user.id)


class ExerciseViewSet(ListModelMixin, GenericViewSet):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer

    def get_queryset(self):
        program_id = self.request.query_params.get('program_id')
        return self.queryset.filter(
            program__owner_id=self.request.user.id,
            program_id=program_id)
