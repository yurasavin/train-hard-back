from django.urls import include, path

from apps.api.router import router
from apps.api.schemas.view import schema_view


urlpatterns = [
    path('swagger.json', schema_view.without_ui(), name='schema-json'),
    path('swagger.yaml', schema_view.without_ui(), name='schema-yaml'),
    path('swagger/', schema_view.with_ui('swagger'), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc'), name='schema-redoc'),
    path('', include(router.urls)),
]
