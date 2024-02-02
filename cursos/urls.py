from django.urls import path
from .views import (CursoAPIView,
                    CursosAPIView,
                    AvaliacaoAPIView,
                    AvaliacoesAPIView,
                    CursoViewSet,
                    AvaliacaoViewSet,
                    )


from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('cursos', CursoViewSet)
router.register('avaliacoes', AvaliacaoViewSet)


urlpatterns = router.urls
