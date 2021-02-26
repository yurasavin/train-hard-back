from rest_framework import routers

from apps.api.viewsets.programs import (ExerciseUpdateView, ProgramListView,
                                        TrainingDetailView)
from apps.api.viewsets.training_history import (ExerciseDoneViewSet,
                                                TrainingHistoryViewSet)

router = routers.DefaultRouter()
router.register('programs', ProgramListView)
router.register('trainings', TrainingDetailView)
router.register('exercises', ExerciseUpdateView)

router.register('training-history', TrainingHistoryViewSet)
router.register('exercise-done', ExerciseDoneViewSet)
