from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet

from apps.api.serializers.users import UserSerializer
from apps.users.models import User


class UserViewSet(ListModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
