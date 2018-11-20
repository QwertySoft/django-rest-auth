from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
# Importamos los ViewSets de nuestra app
from snippets.views import SnippetViewSet, PublisherViewSet

# Instanciamos el router de REST Framework
router = routers.DefaultRouter()
# Definimos la URL de la API para los snippets
router.register('snippets', SnippetViewSet)
# Definimos la URL de la API para los publishers
router.register('publishers', PublisherViewSet)

urlpatterns = [
    # Incluimos las URLs de nuestros ViewSets
    path('api/', include(router.urls)),
    # Incluimos las URLs de la app rest_auth 
    path('rest-auth/', include('rest_auth.urls')),
    # Incluimos las URLs del admin site
    path('admin/', admin.site.urls),
]
