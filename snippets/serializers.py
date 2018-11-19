# Importamos los modelos de nuestra app
from rest_framework import serializers
# Importamos los modelos de nuestra app
from .models import Snippet, Publisher

# Definimos un model serializer para el Publisher
class PublisherSerializer(serializers.ModelSerializer):
    # Epecificamos meta-datos
    class Meta:
        # Estamos definiciendo un serializador para el modelo Snippet
        model = Publisher
        # Idicamos que campos se van a tener en cuenta para la des/serializacion de Publisher
        fields = ('id', 'name')

# Definimos un model serializer para el Snippet
class SnippetSerializer(serializers.ModelSerializer):
    created = serializers.DateTimeField(read_only=True)
    # Definimos el serializador a usar para el Publisher de un Snippet
    publisher = PublisherSerializer(read_only=True)
    # Utilizamos un campo para actualizar la referencia (clave foránea) de un Snippet a un Publisher
    publisher_id = serializers.IntegerField(required=False)

    # Epecificamos meta-datos
    class Meta:
        # Estamos definiciendo un serializador para el modelo Snippet
        model = Snippet
        # Idicamos que campos se van a tener en cuenta para la des/serializacion
        fields = ('id', 'title', 'code', 'language', 'created', 'publisher', 'publisher_id')

