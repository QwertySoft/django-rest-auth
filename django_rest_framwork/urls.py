from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# Importamos los ViewSet de nuestra app
from snippets.views import SnippetViewSet, PublisherViewSet

router = routers.DefaultRouter() # Instanciamos el router de REST Framework
router.register('snippets', SnippetViewSet) # Definimos la URL de la API para los snippets
router.register('publishers', PublisherViewSet) # Definimos la URL de la API para los publishers

urlpatterns = [
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
