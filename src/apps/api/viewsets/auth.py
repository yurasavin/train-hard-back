from django.conf import settings

from rest_framework import status
from rest_framework.response import Response

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)


COOKIE_TOKEN_NAME = 'refresh-token'  # noqa: S105
COOKIE_TOKEN_MAX_AGE = 60 * 60 * 24 * 40


class LoginView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        refresh_token = response.data.pop('refresh')
        response.set_cookie(
            COOKIE_TOKEN_NAME,
            refresh_token,
            path='/api/v1/auth/',
            max_age=COOKIE_TOKEN_MAX_AGE,
            secure=not settings.DEBUG,
            httponly=True,
            samesite='strict',
        )
        return response


class CustomTokenRefreshView(TokenRefreshView):

    def get_serializer(self, *args, **kwargs):
        refresh_token = self.request.COOKIES.get(COOKIE_TOKEN_NAME)
        if refresh_token:
            kwargs['data']['refresh'] = refresh_token
        return super().get_serializer(*args, **kwargs)


class LogoutView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        token = RefreshToken(request.COOKIES.get(COOKIE_TOKEN_NAME))
        token.blacklist()
        response = Response(status=status.HTTP_200_OK)
        response.delete_cookie(COOKIE_TOKEN_NAME)
        return response
