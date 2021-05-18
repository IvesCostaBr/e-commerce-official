from django.db import models

# Create your models here.

class Produto(models.Model):
    titulo = models.CharField(max_length=90)
    bio = models.CharField(max_length=600, blank=True, null=True)
    image_protudo = models.FileField(upload_to=f'produto{id}/', blank=True, null=True)
    preco = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.id  + '  ' + self.titulo
