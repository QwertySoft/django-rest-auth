from django.db import models # Importamos el modulo models de Django

# Declaramos un arreglo de opciones
LANGUAGE_CHOICES = [
    ('PYTHON', 'Python'),
    ('JAVA', 'Java'),
    ('PHP', 'PHP'),
]

# Definimos nuestro modelo Pusblisher
class Publisher(models.Model):
    # Declaramos el campo name
    name = models.CharField(max_length=70, blank=True, default='')

# Definimos nuestro modelo Snippet
class Snippet(models.Model):
    # Declaramos el campo created
    created = models.DateTimeField(auto_now_add=True)
    # Declaramos el campo title
    title = models.CharField(unique=True, max_length=100, blank=True, default='')
    # Declaramos el campo code
    code = models.TextField(blank=True)
    # Declaramos el campo language
    language = models.CharField(choices=LANGUAGE_CHOICES, default='python', max_length=100)
    #Declaramos el campo publisher
    publisher = models.ForeignKey(Publisher, null=True, on_delete=models.CASCADE)

    # Declaramos los metadatos
    class Meta:
        # Indicamos que el orden por defecto de los snippets es por fecha de creacion descendiente
        ordering = ('-created',)