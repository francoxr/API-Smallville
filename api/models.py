from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField("Nombre", max_length=255)
    created = models.DateTimeField('creado',auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

class Quotes(models.Model):
    content = models.CharField(max_length=1000)
    author_id = models.ForeignKey(Author, on_delete=models.CASCADE)
    created = models.DateTimeField('creado',auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

