# Importamos DjangoFilterBackend
from django_filters.rest_framework import DjangoFilterBackend
# Importamos el modulo de viewsets
from rest_framework import viewsets, filters
# Importamos los serializadores de nuestra app
from snippets.serializers import SnippetSerializer, PublisherSerializer
# Importamos los modelos de nuestra app
from snippets.models import Snippet, Publisher

# Definimos el ViewSet para el Snippet
class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve all snippets.
    """
    # Indicamos el QuerySet para listar todos los snippets
    queryset = Snippet.objects.all()
    # Definimos que seralizador usar para transformar los datos devueltos por el QuerySet a JSON
    serializer_class = SnippetSerializer
    # Definimos el uso de un filtro DjangoFilterBackend, SearchFilter y además OrderingFilter
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # Definimos filtros por igualdad por los campos 'title' y 'language'
    filter_fields = ('title', 'language')
    # Definimo un SearchFilter por los campos 'title'
    search_fields = ('title', 'publisher__name')
    # Definimos un orden por defecto a nivel vista que sobreescribe el que define el modelo
    ordering = ('created',)
    # Habilitamos para que se pueda ordenar por los campos 'created' y 'title'
    ordering_fields = ('created', 'title',)

# Definimos el ViewSet para el Publisher
class PublisherViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows retrieve all publishers.
    """
    # Indicamos el QuerySet para listar todos los snippets
    queryset = Publisher.objects.all()
    # Definimos que seralizador usar para transformar los datos devueltos por el QuerySet a JSON
    serializer_class = PublisherSerializer