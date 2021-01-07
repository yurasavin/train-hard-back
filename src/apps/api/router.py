from rest_framework import routers

from apps.api.viewsets.programs import ExerciseViewSet, ProgramViewSet
from apps.api.viewsets.training_history import (
    ExerciseDoneViewSet, TrainingHistoryViewSet)
from apps.api.viewsets.users import UserViewSet


router = routers.DefaultRouter()
router.register('exercises', ExerciseViewSet, basename='exercises')
router.register('programs', ProgramViewSet, basename='programs')
router.register(
    'training-history', TrainingHistoryViewSet, basename='training-history')
router.register('exercise-done', ExerciseDoneViewSet, basename='exercise-done')
router.register('users', UserViewSet, basename='users')
