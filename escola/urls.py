from django.contrib import admin
from django.urls import path, include
from cursos.urls import router
from rest_framework import permissions

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema = get_schema_view(
    openapi.Info(
        title="Escola API",
        default_version='v1.0.0',
        description='''
        Bem-vindo à documentação da API de Gerenciamento de Cursos e Avaliações!
        Esta API foi desenvolvida com o objetivo de proporcionar uma plataforma escalável
        para gerenciar cursos e suas respectivas avaliações em uma plataforma de ensino virtual.
        ''',
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@snippets.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('rest_framework.urls')),
    path('api/v1/', include('cursos.urls')),

    path('api/v2/', include(router.urls)),

    path('swagger<format>/', schema.without_ui(cache_timeout=0), name='json'),
    path('swagger/', schema.with_ui('swagger', cache_timeout=0), name='swagger'),
    path('redoc/', schema.with_ui('redoc', cache_timeout=0), name='redoc'),
]
