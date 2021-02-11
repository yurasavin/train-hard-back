from django.urls import include, path

from apps.api.router import router
from apps.api.schemas.view import schema_view
from apps.api.viewsets import auth

urlpatterns = [
    path('swagger.json', schema_view.without_ui()),
    path('swagger.yaml', schema_view.without_ui()),
    path('swagger/', schema_view.with_ui('swagger')),
    path('auth/login/', auth.LoginView.as_view()),
    path('auth/logout/', auth.LogoutView.as_view()),
    path('auth/access/', auth.CustomTokenRefreshView.as_view()),
    path('redoc/', schema_view.with_ui('redoc')),
    path('', include(router.urls)),
]
