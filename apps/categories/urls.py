from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet

router = DefaultRouter()

router.register(r"", CategoryViewSet, basename = "categories")

urlpatterns = router.urls


# Rutas generadas automáticamente por DRF:
#
# GET     /categories/          → list()            (listar categorías)
# POST    /categories/          → create()          (crear categoría)
# GET     /categories/{id}/     → retrieve()        (obtener una categoría)
# PUT     /categories/{id}/     → update()          (actualizar completa)
# PATCH   /categories/{id}/     → partial_update()  (actualización parcial)
# DELETE  /categories/{id}/     → destroy()         (eliminar)
#
# Extra:
# GET     /                     → API Root (solo con DefaultRouter)

